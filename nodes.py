import comfy.sd


class DaisyChainTextMittimi:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
            "optional": {
                "text_that_comes_first": ("STRING", ),
            },
        }
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("text", )
    FUNCTION = "daisyChainTextMittimi"
    CATEGORY = "mittimiTools"

    def daisyChainTextMittimi(self, text, text_that_comes_first="", ):

        return(text_that_comes_first+text, )
 

NODE_CLASS_MAPPINGS = {
    "DaisyChainTextMittimi": DaisyChainTextMittimi,   
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "DaisyChainTextMittimi": "DaisyChainText", 
}
