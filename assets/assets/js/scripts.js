(function (window, undefined) {
  'use strict';

  /*
  NOTE:
  ------
  PLACE HERE YOUR OWN JAVASCRIPT CODE IF NEEDED
  WE WILL RELEASE FUTURE UPDATES SO IN ORDER TO NOT OVERWRITE YOUR JAVASCRIPT CODE PLEASE CONSIDER WRITING YOUR SCRIPT HERE.  */

  $("#fpoic").click(function(){
  	$("#fpoicon").removeAttr("src");
    $("#fpoicon").attr("src", "app-assets/images/svg/fpo-white.svg");
  });

	$("#basicform").hide();
	$("#addressform").hide();
	$("#officeproofform").hide();
	$("#regdocsform").hide();
	$("#subscribedetailsform").hide();
	$("#docssubscribersform").hide();
	$("#bankdetailsform").hide();
	$("#ceoinfoform").hide();
	$("#accountinfoform").hide();
  $("#authorizedsharedcapitalform").hide();


	// basicform

  $("#basic1").click(function(){
  	$("#basicform").show();
  	$("#regform").hide();
  	$("#addressform").hide();
	$("#officeproofform").hide();
	$("#regdocsform").hide();
	$("#subscribedetailsform").hide();
	$("#docssubscribersform").hide();
	$("#bankdetailsform").hide();
	$("#ceoinfoform").hide();
	$("#accountinfoform").hide();
  });

  	// adressform

  $("#address1").click(function(){
  	$("#basicform").hide();
  	$("#regform").hide();
  	$("#addressform").show();
	$("#officeproofform").hide();
	$("#regdocsform").hide();
	$("#subscribedetailsform").hide();
	$("#docssubscribersform").hide();
	$("#bankdetailsform").hide();
	$("#ceoinfoform").hide();
	$("#accountinfoform").hide();
  });


  // officeproofform

  $("#officeproof1").click(function(){
  	$("#basicform").hide();
  	$("#regform").hide();
  	$("#addressform").hide();
	$("#officeproofform").show();
	$("#regdocsform").hide();
	$("#subscribedetailsform").hide();
	$("#docssubscribersform").hide();
	$("#bankdetailsform").hide();
	$("#ceoinfoform").hide();
	$("#accountinfoform").hide();
  });


  // regdocsform

  $("#regdocs1").click(function(){
  	$("#basicform").hide();
  	$("#regform").hide();
  	$("#addressform").hide();
	$("#officeproofform").hide();
	$("#regdocsform").show();
	$("#subscribedetailsform").hide();
	$("#docssubscribersform").hide();
	$("#bankdetailsform").hide();
	$("#ceoinfoform").hide();
	$("#accountinfoform").hide();
  });


  // subscribedetailsform

  $("#subscribedetails1").click(function(){
  	$("#basicform").hide();
  	$("#regform").hide();
  	$("#addressform").hide();
	$("#officeproofform").hide();
	$("#regdocsform").hide();
	$("#subscribedetailsform").show();
	$("#docssubscribersform").hide();
	$("#bankdetailsform").hide();
	$("#ceoinfoform").hide();
	$("#accountinfoform").hide();
  });


   // docssubscribers1form

  $("#docssubscribers1").click(function(){
  	$("#basicform").hide();
  	$("#regform").hide();
  	$("#addressform").hide();
	$("#officeproofform").hide();
	$("#regdocsform").hide();
	$("#subscribedetailsform").hide();
	$("#docssubscribersform").show();
	$("#bankdetailsform").hide();
	$("#ceoinfoform").hide();
	$("#accountinfoform").hide();
  });

  // bankdetails1form

  $("#bankdetails1").click(function(){
  console.log('bbbbbbbbbbbbbbbb');
  	$("#basicform").hide();
  	$("#regform").hide();
  	$("#addressform").hide();
	$("#officeproofform").hide();
	$("#regdocsform").hide();
	$("#subscribedetailsform").hide();
	$("#docssubscribersform").hide();
	$("#bankdetailsform").show();
	$("#ceoinfoform").hide();
	$("#accountinfoform").hide();
  });



  $("#authorizedsharedcapital1").click(function(){
    $("#authorizedsharedcapitalform").show();
    });



  // ceoinfo1form

  $("#ceoinfo1").click(function(){
  console.log('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
      $("#ceoinfoform").show();
      $("#basicform").hide();
      $("#regform").hide();
      $("#addressform").hide();
    $("#officeproofform").hide();
    $("#regdocsform").hide();
    $("#subscribedetailsform").hide();
    $("#docssubscribersform").hide();
    $("#bankdetailsform").hide();
    $("#accountinfoform").hide();
  $("#authorizedsharedcapitalform").hide();
  $("#issuedsharedcapitalform").hide();
    $("#authorizedsharedcapitalform").hide();
    $("#companymeetingdetailform").hide();
  });

  // accountinfo1form

  $("#accountinfo1").click(function(){

  $("#accountinfoform").show();
      $("#basicform").hide();
      $("#regform").hide();
      $("#addressform").hide();
    $("#officeproofform").hide();
    $("#regdocsform").hide();
    $("#subscribedetailsform").hide();
    $("#docssubscribersform").hide();
    $("#bankdetailsform").hide();
    $("#ceoinfoform").hide();
  $("#issuedsharedcapitalform").hide();
    $("#authorizedsharedcapitalform").hide();
    $("#companymeetingdetailform").hide();

  });


  // $("#authorizedsharedcapital1").click(function(){
  //   $("#basicform").hide();
  //   $("#regform").hide();
  //   $("#addressform").hide();
  // $("#officeproofform").hide();
  // $("#regdocsform").hide();
  // $("#subscribedetailsform").hide();
  // $("#docssubscribersform").hide();
  // $("#bankdetailsform").hide();
  // $("#ceoinfoform").hide();
  // $("#accountinfoform").hide();
  // $("#authorizedsharedcapitalform").show();
  // });


  $("#fpocainfo1").click(function(){
    $("#fpocainformationform").show();
    $("#basicform").hide();
    $("#regform").hide();
    $("#addressform").hide();
    $("#officeproofform").hide();
    $("#regdocsform").hide();
    $("#subscribedetailsform").hide();
    $("#docssubscribersform").hide();
    $("#bankdetailsform").hide();
    $("#ceoinfoform").hide();
    $("#accountinfoform").hide();
    $("#issuedsharedcapitalform").hide();
    $("#authorizedsharedcapitalform").hide();
    $("#companymeetingdetailform").hide();
    });


  $("#reg1").click(function(){
  	$("#basicform").hide();
  	$("#regform").show();
  	$("#addressform").hide();
	$("#officeproofform").hide();
	$("#regdocsform").hide();
	$("#subscribedetailsform").hide();
	$("#docssubscribersform").hide();
	$("#bankdetailsform").hide();
	$("#ceoinfoform").hide();
	$("#accountinfoform").hide();
  });
  
   $(".btn-box1").hide();
  $(".btn-box2").hide();
   $(".btn-box3").hide();
    $(".btn-box4").hide();
     $(".btn-box5").hide();
      $(".btn-box6").hide();
       $(".btn-box7").hide();
        $(".btn-box8").hide();
         $(".btn-box9").hide();
          $(".btn-box10").hide();

//  $("#dsubscriber").hide();
  
//  $("#osubscriber").hide();

  $(".edit1").click(function(){
  	$(".btn-box1").show();
  	$('.f1').removeAttr("disabled");
  });

  $(".edit2").click(function(){
  	$(".btn-box2").show();
  	$('.f2').removeAttr("disabled");
  });


  $(".edit3").click(function(){
  	$(".btn-box3").show();
  	$('.f3').removeAttr("disabled");
  });


$(".edit4").click(function(){
  	$(".btn-box4").show();
  	$('.f4').removeAttr("disabled");
  });


$(".edit5").click(function(){
  	$(".btn-box5").show();
  	$('.f5').removeAttr("disabled");
  });

$(".edit6").click(function(){
  	$(".btn-box6").show();
  	$('.f6').removeAttr("disabled");
  });

$(".edit7").click(function(){
  	$(".btn-box7").show();
  	$('.f7').removeAttr("disabled");
  });

$(".edit8").click(function(){
  	$(".btn-box8").show();
  	$('.f8').removeAttr("disabled");
  });

$(".edit9").click(function(){
  	$(".btn-box9").show();
  	$('.f9').removeAttr("disabled");
  });

$(".edit10").click(function(){
  	$(".btn-box10").show();
  	$('.f10').removeAttr("disabled");
  });


//  $("#inlineRadioOptions1").click(function(){
//  	$("#dsubscriber").show();
//  	$("#osubscriber").hide();
//  });
//
//  $("#inlineRadioOptions2").click(function(){
//  	$("#osubscriber").show();
//  	$("#dsubscriber").hide();
//  });
  $("#d1").click(function(){
    $("#subscriberdatatab").show();
    $("#selctionform").hide();
    $("#dsubscriber").hide();
  });

  $("#d2").click(function(){
    $("#subscriberdatatab").show();
    $("#selctionform").hide();
    $("#osubscriber").hide();
  });

$("#subscribertype").hide();

$("#subadd").click(function(){
  	$("#subscribertype").show();
  	$("#subscriberbox").hide();
    $("#selctionform").show();
  });


$(".fpolist").click(function(){
	var x=$(this).html();
  	$(".fpon").html(x);
  });

$(".fpolist1").click(function(){
  var x=$(this).html();
    $(".fpon1").html(x);
  });


$(".previewimg").hide();

$(".fpolist").click(function(){
  var x=$(this).html();
    $(".fpon").html(x);
  });

$("#subscriberdatatab").hide();

$("#subscribersformlist").hide();
$("#directorcumsubscriberbtn").hide();
$("#docsubscriberbtn").hide();
$("#directorcumsubscriberbtn1").hide();


$(".subscriberdetailform").click(function(){
  $("#subscribersformlist").show();
  $("#subscriberdatatab").hide();
  });


$(".rightediticon").click(function(){
  $("#fusername").removeAttr("disabled");
  $("#directorcumsubscriberbtn").show();
  });


$(".rightediticon1").click(function(){
  $(".dform").removeAttr("disabled");
  $("#docsubscriberbtn").show();
  });


// farmer page

$("#subscriberdetailsfarmer1").click(function(){
  $("#subscriberdetailsformfarmer").show();
  });

  $(".btn-boxfr1").hide();

$(".editfr1").click(function(){
    $(".btn-boxfr1").show();
    $('.fr1').removeAttr("disabled");
  });

// $(".repeatbtn").click(function(){
//   $(".form_repeating").clone().appendTo(".repeatbody");
// });


})(window);



