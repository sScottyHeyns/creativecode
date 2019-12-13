function setup() {
  createCanvas(1300,600);
  
  angleMode(RADIANS);
  
  //Color to Number Translation
  zr= [0,0,0];
  on= [201,40,40];
  tw= [67,120,0];
  thr= [233,185,0];
  fr= [34,57,153];
  fv= [217,111,6];
  sx= [65,200,240];
  svn=[15,76,129];
  eght= [68,49,51];
  nne= [15,76,129];
  clr= [zr,on,tw,thr,fr,fv,sx,svn,eght,nne];
  
  counter= 0;
  
  frameRate(60);
  
  //Sets starting positions for balls
  sec_phase= 0;
  min_phase= 60 - second();
  hour_phase= 3600 - ((minute()*60) + second());
}

function draw() {
  background(19,75,99);
  frm_cnt= frameCount/60;
  
  //Initiate and Update top blocks
  hr_one= (hour()%12)%10;
  hr_ten= ((hour()%12) - hr_one)/10;
  min_one= minute()%10;
  min_ten= (minute() - min_one)/10;
  sec_one= second()%10;
  sec_ten= (second() - sec_one)/10;
  
  //Color Explanation
  fill(zr[0],zr[1],zr[2]);
  zero= rect(width/21,(height*9)/20,width/21,height/10);
  fill(on[0],on[1],on[2]);
  one= rect((width*3)/21,(height*9)/20,width/21,height/10);
  fill(tw[0],tw[1],tw[2]);
  two= rect((width*5)/21,(height*9)/20,width/21,height/10);
  fill(thr[0],thr[1],thr[2]);
  three= rect((width*7)/21,(height*9)/20,width/21,height/10);
  fill(fr[0],fr[1],fr[2]);
  four= rect((width*9)/21,(height*9)/20,width/21,height/10);
  fill(fv[0],fv[1],fv[2]);
  five= rect((width*11)/21,(height*9)/20,width/21,height/10);
  fill(sx[0],sx[1],sx[2]);
  six= rect((width*13)/21,(height*9)/20,width/21,height/10);
  fill(svn[0],svn[1],svn[2]);
  seven= rect((width*15)/21,(height*9)/20,width/21,height/10);
  fill(eght[0],eght[1],eght[2]);
  eight= rect((width*17)/21,(height*9)/20,width/21,height/10);
  fill(nne[0],nne[1],nne[2]);
  nine= rect((width*19)/21,(height*9)/20,width/21,height/10);

  //Draw and update colors of clock
  fill(clr[hr_ten][0],clr[hr_ten][1],clr[hr_ten][2]);
  hr_tens= rect(width/10,0,width/10,height/10);
  fill(clr[hr_one][0],clr[hr_one][1],clr[hr_one][2]);
  hr_ones= rect(width/5,0,width/10,height/10);
  
  fill(clr[min_ten][0],clr[min_ten][1],clr[min_ten][2]);
  min_tens= rect((width*2)/5,0,width/10,height/10);
  fill(clr[min_one][0],clr[min_one][1],clr[min_one][2]);
  min_ones= rect(width/2,0,width/10,height/10);
  
  fill(clr[sec_ten][0],clr[sec_ten][1],clr[sec_ten][2]);
  sec_tens= rect((width*7)/10,0,width/10,height/10);
  fill(clr[sec_one][0],clr[sec_one][1],clr[sec_one][2]);
  sec_ones= rect((width*4)/5,0,width/10,height/10);
  
  fill(255);
  //Update balls
  sec_height= ((height/8.5)*abs(sin((2*PI*frm_cnt)-sec_phase))) + ((17.25*height/20)*abs(cos((2*PI*frm_cnt)-sec_phase)));
  min_height= (((height*3)/20)*abs(sin((PI*frm_cnt/60)-min_phase))) + (((height*5)/6)*abs(cos((PI*frm_cnt/60)-min_phase)));
  hr_height= ((height/5)*abs(sin((PI*frm_cnt/1800)-hour_phase))) + ((height*3/10)*abs(cos((PI*frm_cnt/1800)-hour_phase)));
  hr_ball= circle((width/5),hr_height,(height/5));
  min_ball= circle((width/2),min_height,(height/10));
  sec_ball= circle(((width*4)/5),sec_height,(height/20));
  
  //bottom bar, whose color changes every 25 frames
  fill(clr[counter][0],clr[counter][1],clr[counter][2]);
  if((frameCount%25) == 0){
    counter= (counter+1) % 10;
  }
  bottom= rect(width/15,(height*9)/10,(width*13)/15,height/10);
}
