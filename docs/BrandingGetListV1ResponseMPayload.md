# BrandingGetListV1ResponseMPayload

Payload for GET /1/object/branding/getList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_branding** | [**List[BrandingListElement]**](BrandingListElement.md) |  | 

## Example

```python
from eZmaxApi.models.branding_get_list_v1_response_m_payload import BrandingGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingGetListV1ResponseMPayload from a JSON string
branding_get_list_v1_response_m_payload_instance = BrandingGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print BrandingGetListV1ResponseMPayload.to_json()

# convert the object into a dict
branding_get_list_v1_response_m_payload_dict = branding_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of BrandingGetListV1ResponseMPayload from a dict
branding_get_list_v1_response_m_payload_form_dict = branding_get_list_v1_response_m_payload.from_dict(branding_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


