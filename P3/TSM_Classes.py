import numpy as np
#import TSM_UtilityFunctions as TSM_u
from matplotlib.ticker import Locator

def round_to_1(x):
   if x == 0:
      return 0
   elif -1 < x < 0:
      return np.round(x - 1, -int(np.ceil(np.log10(abs(x)))))
   else:
      return np.round(x, -int(np.ceil(np.log10(abs(x)))))

class MinorSymLogLocator(Locator):
	"""
	Dynamically find minor tick positions based on the positions of
	major ticks for a symlog scaling.
	"""
	
	def __init__(self, linthresh):
		"""
		Ticks will be placed between the major ticks.
		The placement is linear for x between -linthresh and linthresh,
		otherwise its logarithmically
		"""
		self.linthresh = linthresh
	
	def __call__(self):
		"""Return the locations of the ticks"""
		majorlocs = self.axis.get_majorticklocs()
		axisLimits = self.axis.get_data_interval()

		if axisLimits[1] > majorlocs[-1]:
			majorlocs = np.append(majorlocs, [10 ** np.ceil(np.log10(abs(axisLimits[1])))])
		if axisLimits[0] < majorlocs[0]:
			majorlocs = np.insert(majorlocs, 0, [10 ** np.ceil(np.log10(abs(axisLimits[0])))])

		# iterate through minor locs
		minorlocs = []
		
		# handle the lowest part
		ndivs = 5  # Change this number to get other ticks. 2, 4 and 5 look good
		for i in np.arange(1, len(majorlocs)):
			majorstep = round_to_1(majorlocs[i] - majorlocs[i - 1])
			minorstep = majorstep / ndivs
			if minorstep == 0:
				majorlocs[i] = 1
				majorstep = 1
				minorstep = majorstep / ndivs
			
			if abs(majorlocs[i - 1] + majorstep / 2) < self.linthresh:
				if majorlocs[i] < 0:
					locs = np.arange(majorlocs[i - 1] + majorlocs[i] / 10, majorlocs[i], minorstep)[1:]
				else:
					locs = np.arange(majorlocs[i - 1], majorlocs[i] - majorlocs[i] / 10, minorstep)[1:]
			else:
				if majorlocs[i] < 0:
					locs = np.arange(majorlocs[i - 1], majorlocs[i] + majorlocs[i]/10, minorstep)[1:]
				else:
					locs = np.arange(majorlocs[i - 1] - majorlocs[i] / 10, majorlocs[i], minorstep)[1:]
			minorlocs.extend(locs)
		
		return self.raise_if_exceeds(np.array(minorlocs))
	
	def tick_values(self, vmin, vmax):
		raise NotImplementedError('Cannot get tick locations for a ' '%s type.' % type(self))
