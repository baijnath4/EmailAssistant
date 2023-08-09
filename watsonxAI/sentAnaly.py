from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from pandas import read_csv

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    # "apikey": "c2dd7349-54ad-4711-89f8-a431c0bac68a"
    "apikey": "JtRx74OmC0rsFnWVBYjT2Qm8auOT7KqfrrT_YE0_NpY0"
}

project_id = "dea871bd-1746-474d-aab4-89f31526386e"

model_id = ModelTypes.FLAN_UL2


satisfaction_instruction = """
   Classify this review as positive or negative.\n

   comment: I have had a few recent rentals that have taken a very very long time, with no offer of apology.  In the most recent case, the agent subsequently offered me a car type on an upgrade coupon and then told me it was no longer available because it had just be\n
   satisfaction: 'unsatisfied'\n\n
"""

from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

parameters = {
    GenParams.MAX_NEW_TOKENS: 10
}

from ibm_watson_machine_learning.foundation_models import Model

model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id)

input_text = "I recently purchased the TechPro Wireless Earbuds, and I must say, I'm thoroughly impressed! The sound quality is exceptional, with rich bass and clear highs. Whether I'm listening to my favorite music or taking calls, the audio experience is top-notch. The earbuds fit perfectly in my ears, and I love how they stay in place even during my workouts. "
result = model.generate_text(prompt="Classify this review as positive or negative.".join([satisfaction_instruction, input_text]))
                                    