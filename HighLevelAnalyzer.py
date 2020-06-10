# High Level Analyzer
# For more information and documentation, please go to https://github.com/saleae/logic2-examples


class Hla():

    def __init__(self):
        '''
        Initialize this HLA.

        If you have any initialization to do before any methods are called, you can do it here.
        '''
        pass

    def get_capabilities(self):
        '''
        Return the settings that a user can set for this High Level Analyzer. The settings that a user selects will later be passed into `set_settings`.

        This method will be called first, before `set_settings` and `decode`
        '''

        return {
            'settings': {
                'My String Setting': {
                    'type': 'string',
                },
                'My Number Setting': {
                    'type': 'number',
                    'minimum': 0,
                    'maximum': 100
                },
                'My Choices Setting': {
                    'type': 'choices',
                    'choices': ('A', 'B')
                }
            }
        }

    def set_settings(self, settings):
        '''
        Handle the settings values chosen by the user, and return information about how to display the results that `decode` will return.

        This method will be called second, after `get_capbilities` and before `decode`.
        '''

        if 'My Number Setting' in settings:
            number_setting = settings['My Number Setting']
            # You can do something with the number setting here
            pass

        if 'My String Setting' in settings:
            pass

        if 'My Choices Setting' in settings:
            pass

        # Here you can specify how output frames will be formatted in the Logic 2 UI
        # If no format is given for a type, a default formatting will be used
        # You can include the values from your frame data (as returned by `decode`) by wrapping their name in double braces, as shown below.
        return {
            'result_types': {
                'mytype': {
                    'format': 'Output type: {{type}}, Input type: {{data.input_type}}'
                }
            }
        }

    def decode(self, frame):
        '''
        Handle data frame from input analyzer.

        `frame` will always be of the form:

        {
            'type': 'FRAME_TYPE'
            'start_time': ...,
            'end_time': ...,
            'data': {
                ...
            }
        }

        The `type` and contents of the `data` field will depend on the input analyzer.
        '''

        # Return the data frame itself
        return {
            'type': 'mytype',  # This type matches up with the type returned from `set_settings`
            'start_time': frame['start_time'],
            'end_time': frame['end_time'],
            'data': {
                'input_type': frame['type']
            }
        }
