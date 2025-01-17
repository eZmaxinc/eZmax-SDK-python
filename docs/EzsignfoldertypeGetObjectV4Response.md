# EzsignfoldertypeGetObjectV4Response

Response for GET /4/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignfoldertypeGetObjectV4ResponseMPayload**](EzsignfoldertypeGetObjectV4ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_get_object_v4_response import EzsignfoldertypeGetObjectV4Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeGetObjectV4Response from a JSON string
ezsignfoldertype_get_object_v4_response_instance = EzsignfoldertypeGetObjectV4Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeGetObjectV4Response.to_json())

# convert the object into a dict
ezsignfoldertype_get_object_v4_response_dict = ezsignfoldertype_get_object_v4_response_instance.to_dict()
# create an instance of EzsignfoldertypeGetObjectV4Response from a dict
ezsignfoldertype_get_object_v4_response_from_dict = EzsignfoldertypeGetObjectV4Response.from_dict(ezsignfoldertype_get_object_v4_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


