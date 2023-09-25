# EzsigntemplatepackageCreateObjectV1Request

Request for POST /1/object/ezsigntemplatepackage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackage** | [**List[EzsigntemplatepackageRequestCompound]**](EzsigntemplatepackageRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_create_object_v1_request import EzsigntemplatepackageCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageCreateObjectV1Request from a JSON string
ezsigntemplatepackage_create_object_v1_request_instance = EzsigntemplatepackageCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackageCreateObjectV1Request.to_json()

# convert the object into a dict
ezsigntemplatepackage_create_object_v1_request_dict = ezsigntemplatepackage_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatepackageCreateObjectV1Request from a dict
ezsigntemplatepackage_create_object_v1_request_form_dict = ezsigntemplatepackage_create_object_v1_request.from_dict(ezsigntemplatepackage_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


