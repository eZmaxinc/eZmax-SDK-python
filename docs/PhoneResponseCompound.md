# PhoneResponseCompound

A Phone Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_phone_international** | **bool** | Indicate the phone number is an international phone number. | [optional] 

## Example

```python
from eZmaxApi.models.phone_response_compound import PhoneResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneResponseCompound from a JSON string
phone_response_compound_instance = PhoneResponseCompound.from_json(json)
# print the JSON string representation of the object
print(PhoneResponseCompound.to_json())

# convert the object into a dict
phone_response_compound_dict = phone_response_compound_instance.to_dict()
# create an instance of PhoneResponseCompound from a dict
phone_response_compound_from_dict = PhoneResponseCompound.from_dict(phone_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


