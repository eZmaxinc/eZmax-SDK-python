# EzsigntemplatepublicCreateEzsignfolderV1Response

Response for POST /1/object/ezsigntemplatepublic/createEzsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplatepublicCreateEzsignfolderV1ResponseMPayload**](EzsigntemplatepublicCreateEzsignfolderV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_create_ezsignfolder_v1_response import EzsigntemplatepublicCreateEzsignfolderV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicCreateEzsignfolderV1Response from a JSON string
ezsigntemplatepublic_create_ezsignfolder_v1_response_instance = EzsigntemplatepublicCreateEzsignfolderV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicCreateEzsignfolderV1Response.to_json())

# convert the object into a dict
ezsigntemplatepublic_create_ezsignfolder_v1_response_dict = ezsigntemplatepublic_create_ezsignfolder_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepublicCreateEzsignfolderV1Response from a dict
ezsigntemplatepublic_create_ezsignfolder_v1_response_from_dict = EzsigntemplatepublicCreateEzsignfolderV1Response.from_dict(ezsigntemplatepublic_create_ezsignfolder_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


