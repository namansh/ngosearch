# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ngolist',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('NGO_Name', models.TextField(max_length=200)),
                ('Unique_Id_of_VO_NGO', models.TextField(max_length=200)),
                ('Chief_Functionary', models.TextField(max_length=200)),
                ('Chairman', models.TextField(max_length=200)),
                ('Secretary', models.TextField(max_length=200)),
                ('Treasurer', models.TextField(max_length=200)),
                ('Promoter_Name_1', models.TextField(max_length=200)),
                ('Promoter_Name_2', models.TextField(max_length=200)),
                ('Promoter_Name_3', models.TextField(max_length=200)),
                ('Promoter_Name_4', models.TextField(max_length=200)),
                ('Umbrella_Parent_Organization', models.TextField(max_length=200)),
                ('First_Registration_Details', models.TextField(max_length=200)),
                ('Registered_With', models.TextField(max_length=200)),
                ('Type_of_NGO', models.TextField(max_length=200)),
                ('Registration_No', models.TextField(max_length=200)),
                ('City_of_Registration', models.TextField(max_length=200)),
                ('State_of_Registration', models.TextField(max_length=200)),
                ('Date_of_Registration', models.TextField(max_length=200)),
                ('Copy_of_Registration_Certificate', models.TextField(max_length=200)),
                ('Second_Registration_Details', models.TextField(max_length=200)),
                ('Third_Registration_Details', models.TextField(max_length=200)),
                ('Sector_Key_Issues', models.TextField(max_length=200)),
                ('Key_Issues', models.TextField(max_length=2000)),
                ('Operational_Area_States', models.TextField(max_length=200)),
                ('Details_of_Achievements', models.TextField(max_length=200)),
                ('Major_Activities_Achievements', models.TextField(max_length=2000)),
                ('Contact_Details', models.TextField(max_length=200)),
                ('Address', models.TextField(max_length=2000)),
                ('City', models.TextField(max_length=200)),
                ('State', models.TextField(max_length=200)),
                ('Telephone', models.TextField(max_length=200)),
                ('misc', models.TextField(max_length=200)),
                ('Mobile_No', models.TextField(max_length=200)),
                ('E_mail', models.TextField(max_length=200)),
                ('Operational_Area_District', models.TextField(max_length=200)),
                ('Fax', models.TextField(max_length=200)),
                ('FCRA_details', models.TextField(max_length=200)),
                ('FCRA_Registration_no', models.TextField(max_length=200)),
                ('Valid_up_to', models.TextField(max_length=200)),
                ('Website_Url', models.TextField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
