# EzsigntemplatepackagesignerEditObjectV1Request

Request for PUT /1/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatepackagesigner** | [**EzsigntemplatepackagesignerRequestCompound**](EzsigntemplatepackagesignerRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_edit_object_v1_request import EzsigntemplatepackagesignerEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerEditObjectV1Request from a JSON string
ezsigntemplatepackagesigner_edit_object_v1_request_instance = EzsigntemplatepackagesignerEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerEditObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_edit_object_v1_request_dict = ezsigntemplatepackagesigner_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerEditObjectV1Request from a dict
ezsigntemplatepackagesigner_edit_object_v1_request_from_dict = EzsigntemplatepackagesignerEditObjectV1Request.from_dict(ezsigntemplatepackagesigner_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


