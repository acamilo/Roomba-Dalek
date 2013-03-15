
// center joystick
     var parent = $( "#joystick" );
     var draggable = $( "#draggable" );
     $( "#draggable" ).offset({
          top: (parent.height()/2)-(draggable.height()/2),
          left: (parent.width()/2)-(draggable.width()/2)
     });

var posx = 0;
var posy = 0;
var oldx = 0;
var oldy = 0;

// ajax update
setInterval(function(){
			var frame = $( "#joystick" );
    		var stick = $( "#draggable" );
            if (typeof(frame)!="undefined" & typeof(stick)!="undefined"){
			    posx = ((stick.position().left-frame.position().left)+(stick.width()/2))-(frame.width()/2)+0.5;
			    posy =  ((stick.position().top-frame.position().top)+(stick.height()/2))-(frame.height()/2);

			    // update if position changes
			    if (posx != oldx | posy != oldy){ 
				         var parent = $( "#joystick" );
        				 var draggable = $( "#draggable" );



				    oldx = posx; oldy = posy;
				    $.getJSON('/drive/'+posx+'/'+posy+'',null);
			    }
            } else {console.log("undef");}
},100);

  $(function() {

    $( "#draggable" ).draggable({
          containment: "parent",
          revert: true,
          drag: function(){/*
               var position = $(this).position();
               var parentpos= $(this).parent().position();
               var offseth = ($(this).parent().height()/2)+parentpos.top;
               var offsetw = ($(this).parent().width()/2)+parentpos.left;

               posx = ((position.left+25)-offsetw);
               posy = ((position.top+25)-offseth);*/
          },
          stop:function(){/*
              var position = $(this).position();
               var parentpos= $(this).parent().position();
               var offseth = ($(this).parent().height()/2)+parentpos.top;
               var offsetw = ($(this).parent().width()/2)+parentpos.left;

               posx = ((position.left+25)-offsetw);
               posy = ((position.top+25)-offseth);*/

          }

     });
  });

