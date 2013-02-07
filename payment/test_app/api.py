from tastypie.resources import ModelResource
from models import Record

# sudo smsbox -v 0 /etc/kannel/kannel.conf
# sudo bearerbox -v 0 /etc/kannel/kannel.conf
# sudo ps -ef | grep bearerbox


class RecordResource(ModelResource):
    class Meta:
        queryset = Record.objects.all()
        resource_name = 'record'
