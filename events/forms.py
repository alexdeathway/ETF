from django.forms import ModelForm


class EventCreationForm(ModelForm):
    class Meta:
        
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

class EventTicketTypeCreationForm(ModelForm):
    class Meta:
        
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

class EventTicketBookingForm(ModelForm):
    class Meta:
        
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'        