# EzsignimportfolderGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignimportfolder/{pkiEzsignimportfolderID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignimportfolder** | [**EzsignimportfolderResponseCompound**](EzsignimportfolderResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignimportfolder_get_object_v2_response_m_payload import EzsignimportfolderGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignimportfolderGetObjectV2ResponseMPayload from a JSON string
ezsignimportfolder_get_object_v2_response_m_payload_instance = EzsignimportfolderGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignimportfolderGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignimportfolder_get_object_v2_response_m_payload_dict = ezsignimportfolder_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignimportfolderGetObjectV2ResponseMPayload from a dict
ezsignimportfolder_get_object_v2_response_m_payload_from_dict = EzsignimportfolderGetObjectV2ResponseMPayload.from_dict(ezsignimportfolder_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


