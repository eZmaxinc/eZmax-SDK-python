# EzmaxinvoicingGetProvisionalV1Response

Response for GET /1/object/ezmaxinvoicing/getProvisional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzmaxinvoicingGetProvisionalV1ResponseMPayload**](EzmaxinvoicingGetProvisionalV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicing_get_provisional_v1_response import EzmaxinvoicingGetProvisionalV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingGetProvisionalV1Response from a JSON string
ezmaxinvoicing_get_provisional_v1_response_instance = EzmaxinvoicingGetProvisionalV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingGetProvisionalV1Response.to_json())

# convert the object into a dict
ezmaxinvoicing_get_provisional_v1_response_dict = ezmaxinvoicing_get_provisional_v1_response_instance.to_dict()
# create an instance of EzmaxinvoicingGetProvisionalV1Response from a dict
ezmaxinvoicing_get_provisional_v1_response_form_dict = ezmaxinvoicing_get_provisional_v1_response.from_dict(ezmaxinvoicing_get_provisional_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


