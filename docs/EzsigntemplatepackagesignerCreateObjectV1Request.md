# EzsigntemplatepackagesignerCreateObjectV1Request

Request for POST /1/object/ezsigntemplatepackagesigner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackagesigner** | [**List[EzsigntemplatepackagesignerRequestCompound]**](EzsigntemplatepackagesignerRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_create_object_v1_request import EzsigntemplatepackagesignerCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerCreateObjectV1Request from a JSON string
ezsigntemplatepackagesigner_create_object_v1_request_instance = EzsigntemplatepackagesignerCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerCreateObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_create_object_v1_request_dict = ezsigntemplatepackagesigner_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerCreateObjectV1Request from a dict
ezsigntemplatepackagesigner_create_object_v1_request_form_dict = ezsigntemplatepackagesigner_create_object_v1_request.from_dict(ezsigntemplatepackagesigner_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


