"use client";
import { useState, useEffect, useRef } from "react";
import { getConversations, getMedicines } from "../doctors/test";
import { formatDistanceToNow, parseISO } from "date-fns";

export default function ChatBox({ user, doctor }) {
  const [conversations, setConversations] = useState([]);
  const scrollToRef = useRef(null);
  const websocketRef = useRef(null);

  const updateConversations = async () => {
    try {
      const conversationData = await getConversations(user, doctor);
      const medicineData = await getMedicines(user, doctor);

      if (Array.isArray(conversationData) && Array.isArray(medicineData)) {
        const formattedConversations = conversationData.map((msg) => ({
          ...msg,
          type: "message",
          formattedDate: formatRelativeDate(msg.date),
          isoDate: msg.date, 
        }));

        const formattedMedicines = medicineData.map((med) => ({
          ...med,
          type: "medicine",
          formattedDate: formatRelativeDate(med.date),
          isoDate: med.date, 
        }));

        const mergedData = [...formattedConversations, ...formattedMedicines];
        mergedData.sort((a, b) => parseISO(a.isoDate) - parseISO(b.isoDate)); // Sort using ISO date

        setConversations(mergedData);
      } else {
        console.error("Expected arrays, got:", conversationData, medicineData);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      setConversations([]);
    }
  };

  useEffect(() => {
    updateConversations();
  }, [user, doctor]);

  function formatRelativeDate(dateString) {
    const date = parseISO(dateString);

    return formatDistanceToNow(date, { addSuffix: true });
  }

  useEffect(() => {
    websocketRef.current = new WebSocket(
      `ws://127.0.0.1:8000/ws/chats/${user}/${doctor}/0/`
    );

    websocketRef.current.onopen = () => {
      console.log("WebSocket connected");
    };

    websocketRef.current.onmessage = (event) => {
      const receivedData = JSON.parse(event.data);

      if (receivedData.type === "medicine_message") {
        const medicamentData = {
          ...receivedData.data,
          type: "medicine",
          date: formatRelativeDate(receivedData.data.date),
        };
        setConversations((prevConversations) => [
          ...prevConversations,
          medicamentData,
        ]);
      } else {
        const transformedData = {
          sender: {
            username: receivedData.sender,
          },
          receiver: {
            username: receivedData.receiver,
          },
          content: receivedData.message,
          date: formatRelativeDate(receivedData.date),
          delivered: receivedData.delivered,
        };
        setConversations((prevConversations) => [
          ...prevConversations,
          transformedData,
        ]);
      }
    };

    return () => {
      websocketRef.current.close();
    };
  }, [user, doctor]);

  useEffect(() => {
    if (scrollToRef.current) {
      scrollToRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [conversations]);

  return (
    <div className="flex flex-col w-full p-2 gap-6 min-h-[110dvh] overflow-auto scrollbar-hide py-24">
      {(Array.isArray(conversations) ? conversations : []).map(
        (message, index) => {
          console.log(message.receiver);
          return message.type == "medicine" ? (
            <DataTable key={index} data={message.medicaments} />
          ) : (
            <Message
              key={index}
              {...message}
              incoming={user == message.sender.username ? false : true}
            />
          );
        }
      )}
      <div ref={scrollToRef}></div>
    </div>
  );
}

export const Message = ({
  incoming = true,
  content = "Emerald Walker",
  sender = { username: "John" },
  formattedDate = "52:45 14h",
  receiver = { username: "John" },
}) => {
  return (
    <div className={incoming ? "chat chat-start" : "chat chat-end"}>
      <div className="chat-image avatar">
        <div className="w-10 rounded-full">
          <img src={sender.profile} className="" alt="Profile" />
        </div>
      </div>
      <div className="chat-header">
        {sender.username}
        <time className="text-xs opacity-50 px-2">{formattedDate}</time>
      </div>
      <div
        className={incoming ? "chat-bubble" : "chat-bubble chat-bubble-accent"}
      >
        {content}
      </div>
      <div className="chat-footer opacity-50">Delivered</div>
    </div>
  );
};

export function DataTable({ data }) {
  return (
    <div className="overflow-x-auto bg-base-200 rounded-2xl mx-4">
      <table className="table table-zebra">
        <thead>
          <tr>
            <th></th>
            <th>Name</th>
            <th>Form</th>
            <th>Strenght</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <th>{index + 1}</th>
              <td>{item.name}</td>
              <td>{item.form}</td>
              <td>{item.strenght} mg</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
