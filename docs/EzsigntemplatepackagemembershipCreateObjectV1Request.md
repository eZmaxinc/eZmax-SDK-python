# EzsigntemplatepackagemembershipCreateObjectV1Request

Request for POST /1/object/ezsigntemplatepackagemembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackagemembership** | [**List[EzsigntemplatepackagemembershipRequestCompound]**](EzsigntemplatepackagemembershipRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_create_object_v1_request import EzsigntemplatepackagemembershipCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipCreateObjectV1Request from a JSON string
ezsigntemplatepackagemembership_create_object_v1_request_instance = EzsigntemplatepackagemembershipCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipCreateObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_create_object_v1_request_dict = ezsigntemplatepackagemembership_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipCreateObjectV1Request from a dict
ezsigntemplatepackagemembership_create_object_v1_request_form_dict = ezsigntemplatepackagemembership_create_object_v1_request.from_dict(ezsigntemplatepackagemembership_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


