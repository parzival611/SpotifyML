$(document).ready(function(){
var text;
var tempo=110, acousticness=0.5, liveness=0.5, energy=0.5, valence=0.5, instrumnetalness=0.5, loudness= -.30;
$('a').click(function(){
    var cur = $(this).html();
    console.log(cur);
    var pre = $(this).parent().attr('id');
    if(pre=="TEMPO"){
        if(cur=="Relaxed"){
            (tempo <= 80 && tempo >= 60);
        } else if(cur=="Moderate"){
			(tempo <= 100 && tempo >= 80);
        } else if(cur=="Fast"){ 
        	(tempo <= 120 && tempo >= 100);
        } else if(cur=="Intense"){
        	(tempo <= 140 && tempo >= 120); 
        }
    }
//     if(pre=="ACOUSTICNESS"){
//         if(cur=="All-Acoustic"){
//             (acousticness =< 1.00 && acousticness >= 0.75);
//         } else if(cur=="Mostly Acoustic"){
//         	(acousticness =< 0.75 && acousticness >= 0.50);
//         } else if(cur=="Mostly Digital"){ 
//         	(acousticness =< 0.50 && acousticness >= 0.25);
//         } else if(cur=="Pure Digital"){
//         	(acousticness =< 0.25 && acousticness >= 0.00); 
//         }
//     }
//     if(pre=="LIVENESS"){
//         if(cur=="No Audience"){
//             (liveness =< 0.25 && liveness >= 0.00);
//         } else if(cur=="Small Audience"){
//         	(liveness =< 0.50 && liveness >= 0.25);
//         } else if(cur=="Medium Audience"){ 
//         	(liveness =< 0.75 && liveness >= 0.50);
//         } else if(cur=="Large Audience"){
//         	(liveness =< 1.00 && liveness >= 0.75); 
//         }
//     }
//     if(pre=="ENERGY"){
//         if(cur=="Relaxed"){
//             (energy >= 0.00 && energy <= 0.25);
//         } else if(cur=="Moderate"){
//         	(energy >= 0.25 && energy <= 0.50);
//         } else if(cur=="Hyper"){ 
//         	(energy >= 0.50 && energy <= 0.75);
//         } else if(cur=="Intense"){
//         	(energy >= 0.75 && energy <= 1.00); 
//         }
//     }
//     if(pre=="VALENCE"){
//         if(cur=="Euphoric"){
//             (valence >= 0.75 && valence <= 1.00);
//         } else if(cur=="Positive"){
//         	(valence >= 0.50 && valence <= 0.75);
//         } else if(cur=="Dispirited"){ 
//         	(valence >= 0.25 && valence <= 0.50);
//         } else if(cur=="Melancholic"){
// (valence >= 0.00 && valence <= 0.25);
//         }
//     }
//     if(pre=="INSTRUMETNALNESS"){
//         if(cur=="Pure Instrumental"){
// 			(instrumnetalness >= 0.75 && instrumnetalness <= 1.00);
//         } else if(cur=="Balanced"){
// 			(instrumnetalness >= 0.50 && instrumnetalness <= 0.75);
//         } else if(cur=="Wordy"){
// 			(instrumnetalness >= 0.25 && instrumnetalness <= 0.50);
//         } else if(cur=="Verbose"){
// 			(instrumnetalness >= 0.00 && instrumnetalness <= 0.25);
//         }
//     }
//     if(pre=="LOUDNESS"){
//         if(cur=="Powerful"){
// 			(loudness >= 0.75 && loudness <= 1.00);
//         } else if(cur=="Loud"){
//         	(loudness >= 0.50 && loudness <= 0.75);
//         } else if(cur=="Quiet"){ 
//         	(loudness >= 0.25 && loudness <= 0.50);
//         } else if(cur=="Whisper"){
//         	(loudness >= 0.00 && loudness <= 0.25);
//         }
//     }	

//     text = pre +" "+cur;
//     $("#text").append(text);
//     $("#text").append('<br>');

	// });
	var sendJson={"tempo": tempo, "acousticness": acousticness, "liveness": liveness, "energy": energy, "valence": valence, "instrumnetalness": instrumnetalness, "loudness": loudness};
	// data sent below to resq
	var clicked;
	//ajax posting
	$("#dance").click(function(){
	  clicked ="demo";
	  console.log(clicked);

	  $.ajax({
	    type : 'POST',
	    url : "/",
	    contentType: 'application/json',
	    data : JSON.stringify(sendJson),
	    dataType: "json",  
	}).done(function (request) {});
});