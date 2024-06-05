from rest_framework import serializers
from passenger.models import Passenger, PassengerPhone


class PassengerPhoneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PassengerPhone
        fields = ['id', 'number', 'description']


class PassengerSerializer(serializers.ModelSerializer):
    phones = PassengerPhoneSerializer(many=True)

    class Meta:
        model = Passenger
        fields = ["id", "first_name", "second_name", "patronymic", "category", "phones", "description", "gender",
                  "is_pacemaker"]

    def create(self, validated_data):
        phones = validated_data.pop('phones')
        passenger = Passenger.objects.create(**validated_data)

        for phone in phones:
            PassengerPhone.objects.create(passenger=passenger, **phone)
        return passenger

    def update(self, instance, validated_data):
        phones_data = validated_data.pop('phones', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        incoming_ids = [phone['id'] for phone in phones_data if 'id' in phone]

        for phone in instance.phones.all():
            if phone.id not in incoming_ids:
                phone.delete()

        for phone_data in phones_data:
            phone_id = phone_data.get('id', None)
            if phone_id and PassengerPhone.objects.filter(id=phone_id).exists():

                phone = PassengerPhone.objects.get(id=phone_id)
                phone.number = phone_data.get('number', phone.number)
                phone.description = phone_data.get('description', phone.description)
                phone.save()
            elif phone_id is None:

                PassengerPhone.objects.create(passenger=instance, **phone_data)

        return instance
