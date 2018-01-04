# IIR2_Filter
Python class used to implement second order chain IIR filters


Constructor is used to calculate the coefficients of the filter and set up various arrays/variables
            to be used in the filter
            
            Takes in:
                _order = the order of the filter to by created
                _cutoff = the cutoff frequency(s) of the filter normalised to sample rate
            
            Optional:
                filter_type = defines if the filter is lowpass/bandpass/highpass/bandstop
                analogue_filter = defines the type of analogue filter to be replicated
                cheby_ripple = defines the acceptable ripple in a chebyshev filter in dB
                direct_form = defines if a direct form 1 or 2 filter is to be used
                fixed_point = defines if a direct form 1 filter should be fixed point
                
            Called to instantantiate the class. 
            Example:
              >import IIR_Filter as iir
              >p3 = iir.IIR2Filter(order,cut,filter_type='bandpass',analogue_filter='butter',direct_form=1,fixed_point=False)
                
Filter function implements the IIR filtering operation element by element. Does so for
             the correct number of second order sections as defined in the constructor.
             
             
            Takes in:
                v = input data value to the filter
                
            Returns:
                result = output value from the filter
                
            Called to pass in latest data value.
            Example:
              >filtered_data[i] = p3.filter(data[i])
