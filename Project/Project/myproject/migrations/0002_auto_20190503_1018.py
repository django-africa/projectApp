# Generated by Django 2.1.7 on 2019-05-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='code_num',
            new_name='code_number',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='des',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='id_num',
            new_name='identification_number',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='_class',
            new_name='project_class',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='a_close_date',
            new_name='actual_close_date',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='a_start_date',
            new_name='actual_start_date',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='e_close_date',
            new_name='estimated_close_date',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='e_start_date',
            new_name='estimated_start_date',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='id_num_beneficiary',
            new_name='idenfication_number_of_beneficiary',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='scode_num',
            new_name='subprject_code_number',
        ),
        migrations.RenameField(
            model_name='subproject',
            old_name='sid_num',
            new_name='subproject_idenfication_number',
        ),
        migrations.RenameField(
            model_name='subprojectappriasal',
            old_name='ap_date',
            new_name='appriase_date',
        ),
        migrations.RenameField(
            model_name='subprojectappriasal',
            old_name='a_name',
            new_name='appriaser_name',
        ),
        migrations.RenameField(
            model_name='subprojectappriasal',
            old_name='r_action',
            new_name='remedial_action',
        ),
        migrations.RenameField(
            model_name='subprojectcloseout',
            old_name='a_name',
            new_name='appriaser_name',
        ),
        migrations.RenameField(
            model_name='subprojectcloseout',
            old_name='c_date',
            new_name='closeout_date',
        ),
        migrations.RenameField(
            model_name='subprojectcloseout',
            old_name='close_num',
            new_name='closeout_number',
        ),
        migrations.RenameField(
            model_name='subprojectcloseout',
            old_name='id_num',
            new_name='identification_number',
        ),
        migrations.RenameField(
            model_name='subprojectcloseout',
            old_name='sid_num',
            new_name='subproject_identification_number',
        ),
        migrations.RemoveField(
            model_name='subproject',
            name='spname',
        ),
        migrations.AddField(
            model_name='subproject',
            name='subproject_name',
            field=models.CharField(default='subproject name', max_length=300),
        ),
    ]
