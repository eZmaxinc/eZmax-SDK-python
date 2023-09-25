# PhonestaticResponse

A Phonestatic Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_phonestatic_id** | **int** | The unique ID of the Phone. | 
**s_phonestatic_e164** | **str** | A phone number in E.164 Format | [optional] 
**s_phonestatic_extension** | **str** | The extension of the phone number. | [optional] 

## Example

```python
from eZmaxApi.models.phonestatic_response import PhonestaticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PhonestaticResponse from a JSON string
phonestatic_response_instance = PhonestaticResponse.from_json(json)
# print the JSON string representation of the object
print PhonestaticResponse.to_json()

# convert the object into a dict
phonestatic_response_dict = phonestatic_response_instance.to_dict()
# create an instance of PhonestaticResponse from a dict
phonestatic_response_form_dict = phonestatic_response.from_dict(phonestatic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


