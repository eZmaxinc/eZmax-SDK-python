# EzsigntemplatepackagesignermembershipDeleteObjectV1Response

Response for DELETE /1/object/ezsigntemplatepackagesignermembership/{pkiEzsigntemplatepackagesignermembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload**](EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesignermembership_delete_object_v1_response import EzsigntemplatepackagesignermembershipDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignermembershipDeleteObjectV1Response from a JSON string
ezsigntemplatepackagesignermembership_delete_object_v1_response_instance = EzsigntemplatepackagesignermembershipDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagesignermembershipDeleteObjectV1Response.to_json()

# convert the object into a dict
ezsigntemplatepackagesignermembership_delete_object_v1_response_dict = ezsigntemplatepackagesignermembership_delete_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignermembershipDeleteObjectV1Response from a dict
ezsigntemplatepackagesignermembership_delete_object_v1_response_form_dict = ezsigntemplatepackagesignermembership_delete_object_v1_response.from_dict(ezsigntemplatepackagesignermembership_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


