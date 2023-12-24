# EzsigntemplatepackagesignermembershipCreateObjectV1Response

Response for POST /1/object/ezsigntemplatepackagesignermembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagesignermembershipCreateObjectV1ResponseMPayload**](EzsigntemplatepackagesignermembershipCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesignermembership_create_object_v1_response import EzsigntemplatepackagesignermembershipCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignermembershipCreateObjectV1Response from a JSON string
ezsigntemplatepackagesignermembership_create_object_v1_response_instance = EzsigntemplatepackagesignermembershipCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagesignermembershipCreateObjectV1Response.to_json()

# convert the object into a dict
ezsigntemplatepackagesignermembership_create_object_v1_response_dict = ezsigntemplatepackagesignermembership_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignermembershipCreateObjectV1Response from a dict
ezsigntemplatepackagesignermembership_create_object_v1_response_form_dict = ezsigntemplatepackagesignermembership_create_object_v1_response.from_dict(ezsigntemplatepackagesignermembership_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


