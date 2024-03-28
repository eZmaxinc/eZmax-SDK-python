# EzsignpageResponse

An Ezsignpage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignpage_id** | **int** | The unique ID of the Ezsignpage | 
**i_ezsignpage_widthimage** | **int** | The Width of the page&#39;s image in pixels calculated at 100 DPI | 
**i_ezsignpage_heightimage** | **int** | The Height of the page&#39;s image in pixels calculated at 100 DPI | 
**i_ezsignpage_widthpdf** | **int** | The Width of the page in points calculated at 72 DPI | 
**i_ezsignpage_heightpdf** | **int** | The Height of the page in points calculated at 72 DPI | 
**i_ezsignpage_pagenumber** | **int** | The page number in the Ezsigndocument | 
**s_computed_imageurl** | **str** | The Url to the Ezsignpage&#39;s rasterized image.  Url will expire after 5 minutes. | 

## Example

```python
from eZmaxApi.models.ezsignpage_response import EzsignpageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignpageResponse from a JSON string
ezsignpage_response_instance = EzsignpageResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignpageResponse.to_json())

# convert the object into a dict
ezsignpage_response_dict = ezsignpage_response_instance.to_dict()
# create an instance of EzsignpageResponse from a dict
ezsignpage_response_form_dict = ezsignpage_response.from_dict(ezsignpage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


