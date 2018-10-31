from preprocessing import *
from encoding_circ import *

class QEncoder(object):

	"""
	Base class for a quantum circuit which encodes classical data into a
	quantum state.
	"""

	# Default setting for the quantum encoder. See __init__ for detailed
	# explanations
	QENCODER_OPTIONS_DEFAULT={
		'preprocessing':normalize, 	# see preprocessing.py
		'encoding_circ':x_product,     	# see encoding_circ.py
	}

	def __init__(self, input_vec, qubits_chosen,\
			options=QENCODER_OPTIONS_DEFAULT):

		"""
		Initializes an instance of quantum encoder.

		Args:
			input_vec: list[float]
				An input vector representing the classical data
				point to be encoded.
			qubits_chosen: list[int]
				List of indices for the qubits that the circuit
				acts on.
			options: dictionary
				Further information about the choice of the
				quantum encoding scheme. Entries include
				preprocessing: function handle
					Name of a function which preprocesses
					the input vector into another vector
					which is perhaps more suitable for
					quantum circuit construction.
				encoding_circ: function handle
					Name of a function which takes a
					vector and returns a circuit (a pyquil
					Program object).

		"""

		self.preprocessor = options['preprocessing']
		self.generator = options['encoding_circ']
		self.input_vec = self.preprocessor(input_vec, qubits_chosen)
		self.circuit = self.generator(self.input_vec)
