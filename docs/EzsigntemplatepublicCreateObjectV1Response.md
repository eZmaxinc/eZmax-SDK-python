# EzsigntemplatepublicCreateObjectV1Response

Response for POST /1/object/ezsigntemplatepublic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplatepublicCreateObjectV1ResponseMPayload**](EzsigntemplatepublicCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_create_object_v1_response import EzsigntemplatepublicCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicCreateObjectV1Response from a JSON string
ezsigntemplatepublic_create_object_v1_response_instance = EzsigntemplatepublicCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicCreateObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatepublic_create_object_v1_response_dict = ezsigntemplatepublic_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepublicCreateObjectV1Response from a dict
ezsigntemplatepublic_create_object_v1_response_from_dict = EzsigntemplatepublicCreateObjectV1Response.from_dict(ezsigntemplatepublic_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


