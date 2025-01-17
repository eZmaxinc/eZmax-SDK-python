# EzsigntemplatepackageGetListV1ResponseMPayload

Payload for GET /1/object/ezsigntemplatepackage/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackage** | [**List[EzsigntemplatepackageListElement]**](EzsigntemplatepackageListElement.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_get_list_v1_response_m_payload import EzsigntemplatepackageGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageGetListV1ResponseMPayload from a JSON string
ezsigntemplatepackage_get_list_v1_response_m_payload_instance = EzsigntemplatepackageGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageGetListV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepackage_get_list_v1_response_m_payload_dict = ezsigntemplatepackage_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackageGetListV1ResponseMPayload from a dict
ezsigntemplatepackage_get_list_v1_response_m_payload_from_dict = EzsigntemplatepackageGetListV1ResponseMPayload.from_dict(ezsigntemplatepackage_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


