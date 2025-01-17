from myhdl import block, Signal, intbv,always

@block
def PWMGenerator(pwm_out,clk,duty_cycle,period):
	"""
	PWM Generator hardware design
	
	pwm_out	-- PWM output signal
	clk		-- System clock signal
	duty_cycle	-- Duty cycle (0 to period - 1)
	period		-- PWM period (defines the resolution)
	"""
	
	counter = Signal(intbv(0,min=0,max=period))
	
	@always(clk.posedge)
	def logic():
		if counter < duty_cycle:
			pwm_out.next = 1
		else:
			pwm_out.next = 0
		
		if counter == period-1:
			counter.next = 0
		else:
			counter.next = counter + 1
	
	return logic
