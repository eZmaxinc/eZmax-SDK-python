# EzsigntemplatepackagesignermembershipCreateObjectV1Request

Request for POST /1/object/ezsigntemplatepackagesignermembership

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackagesignermembership** | [**List[EzsigntemplatepackagesignermembershipRequestCompound]**](EzsigntemplatepackagesignermembershipRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesignermembership_create_object_v1_request import EzsigntemplatepackagesignermembershipCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignermembershipCreateObjectV1Request from a JSON string
ezsigntemplatepackagesignermembership_create_object_v1_request_instance = EzsigntemplatepackagesignermembershipCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagesignermembershipCreateObjectV1Request.to_json()

# convert the object into a dict
ezsigntemplatepackagesignermembership_create_object_v1_request_dict = ezsigntemplatepackagesignermembership_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatepackagesignermembershipCreateObjectV1Request from a dict
ezsigntemplatepackagesignermembership_create_object_v1_request_form_dict = ezsigntemplatepackagesignermembership_create_object_v1_request.from_dict(ezsigntemplatepackagesignermembership_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


