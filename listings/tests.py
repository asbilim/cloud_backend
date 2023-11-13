import random
import string
from django.contrib.auth.hashers import make_password
from faker import Faker
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.utils import timezone
from .models import Doctors
import urllib

fake = Faker()

def generate_username():
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return f"doctor_{random_suffix}"

def create_doctor():
    username = generate_username()
    password = make_password("password123")  # Set a default password
    consultation_fee = random.randint(50, 200)
    ratings = random.randint(1, 5)
    description = fake.text()
    profile_image_url = fake.image_url()

    doctor = Doctors.objects.create_user(
        username=username,
        password=password,
        consultation_fee=consultation_fee,
        ratings=ratings,
        description=description
    )

    # Save the profile image
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urllib.request.urlopen(profile_image_url).read())
    img_temp.flush()
    doctor.profile.save(f"profile_{doctor.id}.jpg", File(img_temp))

    return doctor

def create_15_doctors():
    for _ in range(15):
        doctor = create_doctor()
        print(f"Created doctor: {doctor.username}")

