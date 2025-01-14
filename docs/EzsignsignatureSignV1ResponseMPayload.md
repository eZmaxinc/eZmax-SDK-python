# EzsignsignatureSignV1ResponseMPayload

Response for POST /1/object/ezsignsignature/{pkiEzsignsignatureID}/sign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_ezsignsignature_date_in_folder_timezone** | **str** | The date the Ezsignsignature was signed in folder&#39;s timezone | 
**obj_timezone** | [**CustomTimezoneWithCodeResponse**](CustomTimezoneWithCodeResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignature_sign_v1_response_m_payload import EzsignsignatureSignV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureSignV1ResponseMPayload from a JSON string
ezsignsignature_sign_v1_response_m_payload_instance = EzsignsignatureSignV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureSignV1ResponseMPayload.to_json())

# convert the object into a dict
ezsignsignature_sign_v1_response_m_payload_dict = ezsignsignature_sign_v1_response_m_payload_instance.to_dict()
# create an instance of EzsignsignatureSignV1ResponseMPayload from a dict
ezsignsignature_sign_v1_response_m_payload_from_dict = EzsignsignatureSignV1ResponseMPayload.from_dict(ezsignsignature_sign_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


