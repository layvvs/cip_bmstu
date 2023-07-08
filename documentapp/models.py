from django.db import models


class Award(models.Model):
    id_award = models.BigAutoField(db_column='ID_AWARD', primary_key=True)  # Field name made lowercase.
    date_of_award = models.DateField(db_column='Date_of_Award')  # Field name made lowercase.
    award_sum = models.IntegerField(db_column='Award_Sum')  # Field name made lowercase.
    award_term = models.DateField(db_column='Award_Term', blank=True, null=True)  # Field name made lowercase.
    awa_order_num = models.TextField(db_column='AWA_Order_Num', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AWARD'


class Agreements(models.Model):
    ag_p_id_archive = models.OneToOneField('IpcArchive', models.DO_NOTHING, db_column='AG_P_ID_Archive', primary_key=True)  # Field name made lowercase.
    ag_date_of_conclusion = models.DateField(db_column='AG_Date_Of_Conclusion')  # Field name made lowercase.
    ag_num = models.IntegerField(db_column='AG_Num')  # Field name made lowercase.
    ag_date_of_registration = models.DateField(db_column='AG_Date_Of_Registration')  # Field name made lowercase.
    authorized_capital = models.CharField(db_column='Authorized_Capital', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agreements'


class Authors(models.Model):
    p_id_author = models.AutoField(db_column='P_ID_Author', primary_key=True)  # Field name made lowercase.
    author = models.TextField(db_column='Author')  # Field name made lowercase.
    division = models.TextField(db_column='Division')  # Field name made lowercase.
    post = models.TextField(db_column='Post')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Authors'


class Countries(models.Model):
    p_id_countries = models.BigAutoField(db_column='P_ID_Countries', primary_key=True)  # Field name made lowercase.
    co_name = models.TextField(db_column='CO_Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COUNTRIES'


class ConnectingAuthors(models.Model):
    f_id_archive = models.ForeignKey('IpcArchive', models.DO_NOTHING, db_column='F_ID_Archive')  # Field name made lowercase.
    f_id_author = models.ForeignKey(Authors, models.DO_NOTHING, db_column='F_ID_Author')  # Field name made lowercase.
    p_id_cauthors = models.AutoField(db_column='P_ID_CAuthors', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Connecting_Authors'


class ConnectingAwards(models.Model):
    f_id_award = models.ForeignKey(Award, models.DO_NOTHING, db_column='F_ID_Award')  # Field name made lowercase.
    f_id_archive = models.ForeignKey('IpcArchive', models.DO_NOTHING, db_column='F_ID_Archive')  # Field name made lowercase.
    p_id_ca = models.AutoField(db_column='P_ID_CA', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Connecting_Awards'


class ConnectingCountries(models.Model):
    f_id_archive = models.ForeignKey('IpcArchive', models.DO_NOTHING, db_column='F_ID_Archive')  # Field name made lowercase.
    f_id_countries = models.ForeignKey(Countries, models.DO_NOTHING, db_column='F_ID_Countries')  # Field name made lowercase.
    p_id_cc = models.AutoField(db_column='P_ID_CC', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Connecting_Countries'


class ExclusiveRights(models.Model):
    exclusive_rights = models.TextField(db_column='Exclusive_Rights', blank=True, null=True)  # Field name made lowercase.
    p_id_exclusive_rights = models.AutoField(db_column='P_ID_Exclusive_Rights', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exclusive_Rights'


class IpcArchive(models.Model):
    id_archive = models.AutoField(db_column='ID_Archive', primary_key=True)  # Field name made lowercase.
    f_id_object_type = models.ForeignKey('ObjectType', models.DO_NOTHING, db_column='F_ID_Object_Type')  # Field name made lowercase.
    security_doc_num = models.TextField(db_column='Security_Doc_Num')  # Field name made lowercase.
    primary_name = models.TextField(db_column='Primary_Name')  # Field name made lowercase.
    application_num = models.IntegerField(db_column='Application_Num', blank=True, null=True)  # Field name made lowercase.
    application_data = models.DateField(db_column='Application_Data')  # Field name made lowercase.
    final_name = models.TextField(db_column='Final_Name')  # Field name made lowercase.
    responsible_person = models.TextField(db_column='Responsible_Person')  # Field name made lowercase.
    f_official_or_initiative = models.ForeignKey('OfficialOrInitiative', models.DO_NOTHING, db_column='F_Official_or_Initiative')  # Field name made lowercase.
    accounting_in_is = models.CharField(db_column='Accounting_in_IS', max_length=4)  # Field name made lowercase.
    f_id_exclusive_rights = models.ForeignKey(ExclusiveRights, models.DO_NOTHING, db_column='F_ID_Exclusive_Rights')  # Field name made lowercase.
    date_reg_is = models.DateField(db_column='Date_Reg_IS')  # Field name made lowercase.
    next_poshlina_date = models.DateField(db_column='Next_Poshlina_Date', blank=True, null=True)  # Field name made lowercase.
    royalty_payment = models.IntegerField(db_column='Royalty_Payment', blank=True, null=True)  # Field name made lowercase.
    security_document_payment = models.TextField(db_column='Security_Document_Payment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPC_ARCHIVE'


class InitiativePatentTable(models.Model):
    p_in_id_archive = models.OneToOneField(IpcArchive, models.DO_NOTHING, db_column='P_IN_ID_Archive', primary_key=True)  # Field name made lowercase.
    in_contract_num = models.IntegerField(db_column='IN_Contract_Num')  # Field name made lowercase.
    in_contract_date = models.DateField(db_column='IN_Contract_Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Initiative_Patent_Table'


class ObjectType(models.Model):
    object_type = models.CharField(db_column='Object_Type', max_length=40)  # Field name made lowercase.
    f_id_type_of_security_doc = models.ForeignKey('TypeOfSecurityDoc', models.DO_NOTHING, db_column='F_ID_Type_of_Security_Doc')  # Field name made lowercase.
    classifications = models.TextField(db_column='Classifications', blank=True, null=True)  # Field name made lowercase.
    p_id_object_type = models.AutoField(db_column='P_ID_Object_Type', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Object_Type'


class OfficialPatentTable(models.Model):
    p_of_id_archive = models.OneToOneField(IpcArchive, models.DO_NOTHING, db_column='P_OF_ID_Archive', primary_key=True)  # Field name made lowercase.
    of_award_order_num = models.IntegerField(db_column='OF_Award_Order_Num', blank=True, null=True)  # Field name made lowercase.
    of_award_contract_num = models.IntegerField(db_column='OF_Award_Contract_Num', blank=True, null=True)  # Field name made lowercase.
    f_id_official_patent_type = models.ForeignKey('OfficialPatentType', models.DO_NOTHING, db_column='F_ID_Official_Patent_Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Official_Patent_Table'


class OfficialPatentType(models.Model):
    p_id_official_patent_type = models.SmallIntegerField(db_column='P_ID_Official_Patent_Type', primary_key=True)  # Field name made lowercase.
    official_patent_type = models.TextField(db_column='Official_Patent_Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Official_Patent_Type'


class OfficialOrInitiative(models.Model):
    official_or_initiative = models.TextField(db_column='Official_or_Initiative')  # Field name made lowercase.
    p_id_official_or_initiative = models.AutoField(db_column='P_ID_Official_or_Initiative', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Official_or_Initiative'


class TypeOfSecurityDoc(models.Model):
    p_id_type_of_security_doc = models.SmallAutoField(db_column='P_ID_Type_of_Security_Doc', primary_key=True)  # Field name made lowercase.
    type_of_security_doc = models.CharField(db_column='Type_of_Security_Doc', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Type_of_Security_Doc'
