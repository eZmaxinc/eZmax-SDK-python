# EzsigntemplatedocumentpageResponse

An Ezsigntemplatedocumentpage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatedocumentpage_id** | **int** | The unique ID of the Ezsigntemplatedocumentpage | 
**i_ezsigntemplatedocumentpage_widthimage** | **int** | The Width of the page&#39;s image in pixels calculated at 100 DPI | 
**i_ezsigntemplatedocumentpage_heightimage** | **int** | The Height of the page&#39;s image in pixels calculated at 100 DPI | 
**i_ezsigntemplatedocumentpage_widthpdf** | **int** | The Width of the page in points calculated at 72 DPI | 
**i_ezsigntemplatedocumentpage_heightpdf** | **int** | The Height of the page in points calculated at 72 DPI | 
**i_ezsigntemplatedocumentpage_pagenumber** | **int** | The page number in the Ezsigntemplatedocument | 
**s_computed_imageurl** | **str** | The Url to the Ezsigntemplatedocumentpage&#39;s rasterized image.  Url will expire after 5 minutes. | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocumentpage_response import EzsigntemplatedocumentpageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentpageResponse from a JSON string
ezsigntemplatedocumentpage_response_instance = EzsigntemplatedocumentpageResponse.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatedocumentpageResponse.to_json()

# convert the object into a dict
ezsigntemplatedocumentpage_response_dict = ezsigntemplatedocumentpage_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentpageResponse from a dict
ezsigntemplatedocumentpage_response_form_dict = ezsigntemplatedocumentpage_response.from_dict(ezsigntemplatedocumentpage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


