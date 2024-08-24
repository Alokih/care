# Generated by Django 4.2.10 on 2024-07-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facility", "0445_merge_20240715_0301"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hospitaldoctors",
            name="area",
            field=models.IntegerField(
                choices=[
                    (1, "General Medicine"),
                    (2, "Pulmonology"),
                    (3, "Intensivist"),
                    (4, "Pediatrician"),
                    (5, "Others"),
                    (6, "Anesthesiologist"),
                    (7, "Cardiac Surgeon"),
                    (8, "Cardiologist"),
                    (9, "Dentist"),
                    (10, "Dermatologist"),
                    (11, "Diabetologist"),
                    (12, "Emergency Medicine Physician"),
                    (13, "Endocrinologist"),
                    (14, "Family Physician"),
                    (15, "Gastroenterologist"),
                    (16, "General Surgeon"),
                    (17, "Geriatrician"),
                    (18, "Hematologist"),
                    (29, "Immunologist"),
                    (20, "Infectious Disease Specialist"),
                    (21, "MBBS doctor"),
                    (22, "Medical Officer"),
                    (23, "Nephrologist"),
                    (24, "Neuro Surgeon"),
                    (25, "Neurologist"),
                    (26, "Obstetrician/Gynecologist (OB/GYN)"),
                    (27, "Oncologist"),
                    (28, "Oncology Surgeon"),
                    (29, "Ophthalmologist"),
                    (30, "Oral and Maxillofacial Surgeon"),
                    (31, "Orthopedic"),
                    (32, "Orthopedic Surgeon"),
                    (33, "Otolaryngologist (ENT)"),
                    (34, "Palliative care Physician"),
                    (35, "Pathologist"),
                    (36, "Pediatric Surgeon"),
                    (37, "Physician"),
                    (38, "Plastic Surgeon"),
                    (39, "Psychiatrist"),
                    (40, "Pulmonologist"),
                    (41, "Radio technician"),
                    (42, "Radiologist"),
                    (43, "Rheumatologist"),
                    (44, "Sports Medicine Specialist"),
                    (45, "Thoraco-Vascular Surgeon"),
                    (46, "Transfusion Medicine Specialist"),
                    (47, "Urologist"),
                    (48, "Nurse"),
                    (49, "Allergist/Immunologist"),
                    (50, "Cardiothoracic Surgeon"),
                    (51, "Gynecologic Oncologist"),
                    (52, "Hepatologist"),
                    (53, "Internist"),
                    (54, "Neonatologist"),
                    (55, "Pain Management Specialist"),
                    (56, "Physiatrist (Physical Medicine and Rehabilitation)"),
                    (57, "Podiatrist"),
                    (58, "Preventive Medicine Specialist"),
                    (59, "Radiation Oncologist"),
                    (60, "Sleep Medicine Specialist"),
                    (61, "Transplant Surgeon"),
                    (62, "Trauma Surgeon"),
                    (63, "Vascular Surgeon"),
                    (64, "Critical Care Physician"),
                ]
            ),
        ),
    ]