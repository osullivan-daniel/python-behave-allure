# import os

# def before_all(context):
#     print('hello')
#     filepath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..', 'configs/env.json'))
#     with open(filepath) as input:
#         context.api_key = input['tfl']['api_key']
#         print('bye')