     var parent = $( "#joystick" );
     var draggable = $( "#draggable" );
     $( "#draggable" ).offset({
          top: (parent.height()/2)-(draggable.height()/2),
          left: (parent.width()/2)-(draggable.width()/2)
     });


  $(function() {

    $( "#draggable" ).draggable({
          containment: "parent",
          revert: true,
          drag: function(){
               var position = $(this).position();
               var parentpos= $(this).parent().position();
               var offseth = ($(this).parent().height()/2)+parentpos.top;
               var offsetw = ($(this).parent().width()/2)+parentpos.left;

               var posx = ((position.left+25)-offsetw);
               var posy = ((position.top+25)-offseth);
               $.getJSON('/drive/'+posx+'/'+posy+'',null);
          },
          stop:function(){
              var position = $(this).position();
               var parentpos= $(this).parent().position();
               var offseth = ($(this).parent().height()/2)+parentpos.top;
               var offsetw = ($(this).parent().width()/2)+parentpos.left;

               var posx = ((position.left+25)-offsetw);
               var posy = ((position.top+25)-offseth);
               $.getJSON('/drive/'+posx+'/'+posy+'',null);
          }

     });
  });

