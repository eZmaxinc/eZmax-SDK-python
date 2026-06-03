# EzsigndocumentApplyEzsigntemplateglobalV2Request

Request for POST /2/object/ezsigndocument/{pkiEzsigndocumentID}/applyEzsigntemplateglobal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsigntemplateglobal_id** | **int** | The unique ID of the Ezsigntemplateglobal | 
**a_s_ezsigntemplateglobalsigner** | **List[str]** |  | 
**a_fki_ezsignfoldersignerassociation_id** | **List[int]** |  | 
**a_s_ezsigntemplateglobalannotation_description** | **List[str]** |  | [optional] 
**a_s_ezsigntemplateglobalannotation_defaulttext** | **List[str]** |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplateglobal_v2_request import EzsigndocumentApplyEzsigntemplateglobalV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentApplyEzsigntemplateglobalV2Request from a JSON string
ezsigndocument_apply_ezsigntemplateglobal_v2_request_instance = EzsigndocumentApplyEzsigntemplateglobalV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentApplyEzsigntemplateglobalV2Request.to_json())

# convert the object into a dict
ezsigndocument_apply_ezsigntemplateglobal_v2_request_dict = ezsigndocument_apply_ezsigntemplateglobal_v2_request_instance.to_dict()
# create an instance of EzsigndocumentApplyEzsigntemplateglobalV2Request from a dict
ezsigndocument_apply_ezsigntemplateglobal_v2_request_from_dict = EzsigndocumentApplyEzsigntemplateglobalV2Request.from_dict(ezsigndocument_apply_ezsigntemplateglobal_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


