# EzsigntemplatedocumentExtractTextV1Request

Request for POST /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/extractText

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_page** | **int** | The page where the area is located | 
**e_section** | **str** | The section of the page | [optional] 
**i_x** | **int** | The X coordinate (Horizontal). Require when eSection &#x3D; &#39;Region&#39; or eSection is not set. | [optional] 
**i_y** | **int** | The Y coordinate (Vertical). Require when eSection &#x3D; &#39;Region&#39; or eSection is not set. | [optional] 
**i_width** | **int** | Area&#39;s width. Require when eSection &#x3D; &#39;Region&#39; or eSection is not set. | [optional] 
**i_height** | **int** | Area&#39;s height. Require when eSection &#x3D; &#39;Region&#39; or eSection is not set. | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_extract_text_v1_request import EzsigntemplatedocumentExtractTextV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentExtractTextV1Request from a JSON string
ezsigntemplatedocument_extract_text_v1_request_instance = EzsigntemplatedocumentExtractTextV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentExtractTextV1Request.to_json())

# convert the object into a dict
ezsigntemplatedocument_extract_text_v1_request_dict = ezsigntemplatedocument_extract_text_v1_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentExtractTextV1Request from a dict
ezsigntemplatedocument_extract_text_v1_request_from_dict = EzsigntemplatedocumentExtractTextV1Request.from_dict(ezsigntemplatedocument_extract_text_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


