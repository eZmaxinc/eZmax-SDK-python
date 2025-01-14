# EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request

Request for PUT /1/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID}/editEzsigntemplatepackagesigners

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackagesigner** | [**List[EzsigntemplatepackagesignerRequestCompound]**](EzsigntemplatepackagesignerRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request import EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request from a JSON string
ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request_instance = EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request.to_json())

# convert the object into a dict
ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request_dict = ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request_instance.to_dict()
# create an instance of EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request from a dict
ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request_from_dict = EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Request.from_dict(ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


