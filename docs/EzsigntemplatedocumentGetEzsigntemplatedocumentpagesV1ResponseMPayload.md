# EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1ResponseMPayload

Payload for GET /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplatedocumentpages

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatedocumentpage** | [**List[EzsigntemplatedocumentpageResponseCompound]**](EzsigntemplatedocumentpageResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_m_payload import EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1ResponseMPayload from a JSON string
ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_m_payload_instance = EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1ResponseMPayload.to_json()

# convert the object into a dict
ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_m_payload_dict = ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1ResponseMPayload from a dict
ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_m_payload_form_dict = ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_m_payload.from_dict(ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


