# EzsignfolderGetEzsigndocumentsV2ResponseMPayload

Payload for GET /2/object/ezsignfolder/{pkiEzsignfolder}/getEzsigndocuments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigndocument** | [**List[EzsigndocumentResponseCompoundV3]**](EzsigndocumentResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_ezsigndocuments_v2_response_m_payload import EzsignfolderGetEzsigndocumentsV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetEzsigndocumentsV2ResponseMPayload from a JSON string
ezsignfolder_get_ezsigndocuments_v2_response_m_payload_instance = EzsignfolderGetEzsigndocumentsV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetEzsigndocumentsV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignfolder_get_ezsigndocuments_v2_response_m_payload_dict = ezsignfolder_get_ezsigndocuments_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignfolderGetEzsigndocumentsV2ResponseMPayload from a dict
ezsignfolder_get_ezsigndocuments_v2_response_m_payload_from_dict = EzsignfolderGetEzsigndocumentsV2ResponseMPayload.from_dict(ezsignfolder_get_ezsigndocuments_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


