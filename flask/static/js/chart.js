$(function(){
				var data = [
				        	{name : 'UC浏览器',value : 40.0,color:'#4572a7'},
				        	{name : 'QQ浏览器',value : 37.1,color:'#aa4643'},
				        	{name : '欧朋浏览器',value : 13.8,color:'#89a54e'},
				        	{name : '百度浏览器',value : 1.6,color:'#80699b'},
				        	{name : '海豚浏览器',value : 1.4,color:'#92a8cd'},
				        	{name : '天天浏览器',value : 1.2,color:'#db843d'},
				        	{name : '其他',value : 4.9,color:'#a47d7c'}
			        	];

	        	
				var chart = new iChart.Pie2D({
					render : 'canvasDiv',
					data: data,
					title : {
						text : '2012年第3季度中国第三方手机浏览器市场份额',
						color : '#3e576f'
					},
					footnote : {
						text : 'ichartjs.com',
						color : '#486c8f',
						fontsize : 11,
						padding : '0 38'
					},
					sub_option : {
						label : {
							background_color:null,
							sign:false,//设置禁用label的小图标
							padding:'0 4',
							border:{
								enable:false,
								color:'#666666'
							},
							fontsize:11,
							fontweight:600,
							color : '#4572a7'
						},
						border : {
							width : 2,
							color : '#ffffff'
						}
					},
					shadow : true,
					shadow_blur : 6,
					shadow_color : '#aaaaaa',
					shadow_offsetx : 0,
					shadow_offsety : 0,
					background_color:'#fefefe',
					offsetx:-60,//设置向x轴负方向偏移位置60px
					offset_angle:-120,//逆时针偏移120度
					showpercent:true,
					decimalsnum:2,
					width : 800,
					height : 400,
					radius:120
				});
				//利用自定义组件构造右侧说明文本
				chart.plugin(new iChart.Custom({
						drawFn:function(){
							//计算位置
							var y = chart.get('originy'),
								w = chart.get('width');
							
							//在右侧的位置，渲染说明文字
							chart.target.textAlign('start')
							.textBaseline('middle')
							.textFont('600 16px Verdana')
							.fillText('UC浏览器、\n手机QQ浏览器及\n欧朋浏览器的份额\n位列第三方手机浏览器\n市场前三甲',w-220,y-40,false,'#be5985',false,20);
						}
				}));
				
				chart.draw();
			});
		
