# EzsigntemplatepackageEditEzsigntemplatepackagesignersV2Request

Request for PUT /2/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID}/editEzsigntemplatepackagesigners

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackagesigner** | [**List[EzsigntemplatepackagesignerRequestCompoundV2]**](EzsigntemplatepackagesignerRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v2_request import EzsigntemplatepackageEditEzsigntemplatepackagesignersV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageEditEzsigntemplatepackagesignersV2Request from a JSON string
ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v2_request_instance = EzsigntemplatepackageEditEzsigntemplatepackagesignersV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageEditEzsigntemplatepackagesignersV2Request.to_json())

# convert the object into a dict
ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v2_request_dict = ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v2_request_instance.to_dict()
# create an instance of EzsigntemplatepackageEditEzsigntemplatepackagesignersV2Request from a dict
ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v2_request_from_dict = EzsigntemplatepackageEditEzsigntemplatepackagesignersV2Request.from_dict(ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


