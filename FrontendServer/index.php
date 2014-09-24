<?php
	require_once 'config.php';
    $url = $config['ip_address'];
    exec("curl {$url} > /dev/null 2>/dev/null &");
?>

<html xmlns="http://www.w3.org/1999/xhtml" >
<head>
    <title>Welcome</title>
    
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta id="viewport" name="viewport" content="width=320; initial-scale=1.0; maximum-scale=1.0; user-scalable=0;" />
	<link rel="stylesheet" href="public/iphone.css" />
	<link rel="apple-touch-icon" href="public/images/iphone-icon.png" />
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
</head>
<body>
    <div>
        
        <div id="intro">
            <div class="loading">
                <img src='public/images/ajax-loader.gif' />
                <br/>
                Connecting...
            </div>
            <div class="text"></div>
        </div>
        
        <div class="footer">
	        Buzzer Server. &copy; Maciej Zukowski, <?php echo date('y') ?>
	    </div>
	    
    </div>
    <script type='text/javascript'>
    	function buzz () {
	        $.ajax({
	            url:'<?php echo $url ?>',
	            dataType: 'jsonp',
	            complete:function(data,code) {
	            	if (data.status == 200) {
		            	$("#intro .text").html("<img src='public/images/bolt.png' width='100' height='100' /><br />Buzzed!") 
		           	} else {
		            	$("#intro .text").html('Network Down')
		            	
	            	}
	            	$("#intro .loading").hide()
	            }	
	        })
        }
        buzz()

        $("#intro .text").on('click', function() {
	        $("#intro .loading").show()
	        $("#intro .text").html('');
	        buzz();
        });
      
     </script>
</body>
</html>
