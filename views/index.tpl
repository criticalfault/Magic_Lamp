<!DOCTYPE html>
<html>
<head>
	<title>Spooky Lamp Control Panel</title>
	<link 
		href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" 
		rel="stylesheet" 
		integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous" />
	<script
 		src="https://code.jquery.com/jquery-3.2.1.min.js"
  		integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  		crossorigin="anonymous"></script>
</head>
<body>
	<h1 style="text-align: center;">Spooky Lamp v1.0</h1>
	<hr>
		<p style="text-align: center;">Lamp is currently: <span id="power">ON</span> and <span id='color'>WHITE</span> </p>
	<hr>

	<div class='container'>
		<div class='row'>
			<div class='btn btn-success btn-block col-sm-6 col-xs-10' onclick="turnOn()">Turn On</div>
			<div class='btn btn-success btn-block col-sm-6 col-xs-10' onclick="turnOff()">Turn Off</div>
			<div class='btn btn-success btn-block col-sm-6 col-xs-10' onclick="turnRed()">Turn Red</div>
			<div class='btn btn-success btn-block col-sm-6 col-xs-10' onclick="turnBlue()">Turn Blue</div>
			<div class='btn btn-success btn-block col-sm-6 col-xs-10' onclick="turnWhite()">Turn White</div>
		</div>
	<div>
	<hr>
		<div class="btn btn-danger btn-block col-sm-6 col-xs-10">Shutdown Lamp</div>
	<script type="text/javascript">
		
		function turnOff()
		{
			$.ajax({
			  method: "POST",
			  url: "/off",
			})
			  .done(function( ) {
			    $('#power').html('OFF');
			  })
		  .fail(function() {
		    alert( "Connection to the Spooky Lamp couldn't be Established. Contact Dean" );
		 	});
		}

		function turnOn()
		{
			$.ajax({
			  method: "POST",
			  url: "/on",
			})
		  .done(function() {
		    //alert( "Lamp is now ON" );
		    $('#power').html('ON');
		  })
		  .fail(function() {
		    alert( "Connection to the Spooky Lamp couldn't be Established. Contact Dean" );
		 	});
		}

		function turnRed()
		{
			$.ajax({
			  method: "POST",
			  url: "/colorRed",
			}).done(function() {
		    $('#color').html('RED');
		  })
		  .fail(function() {
		    alert( "Connection to the Spooky Lamp couldn't be Established. Contact Dean" );
		 	});
		}

		function turnBlue()
		{
			$.ajax({
			  method: "POST",
			  url: "/colorBlue",
			}).done(function() {
		    $('#color').html('RED');
		  })
		  .fail(function() {
		    alert( "Connection to the Spooky Lamp couldn't be Established. Contact Dean" );
		 	});
		}


		function turnWhite()
		{
			$.ajax({
			  method: "POST",
			  url: "/colorWhite",
			})
		  .done(function() {
		    $('#color').html('WHITE');
		  })
		  .fail(function() {
		    alert( "Connection to the Spooky Lamp couldn't be Established. Contact Dean" );
		 	});
		}

	</script>
</body>
</html>