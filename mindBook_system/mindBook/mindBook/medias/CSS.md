# CSS

根据作用分类

### 布局

flex - 弹性布局

- flex-direction - 容器内项目的排列方式（默认横向排列）
  - row - 默认，沿着水平主轴由左至右排列
  - row-reverse - 沿着水平主轴由右至左排列
  - column - 沿垂直主轴由上到下
  - column-reverse - 沿垂直主轴由下到上
- flex-wrap - 容器内项目换行方式
  - nowrap - 默认，不换行
  - warp - 换行，第一行在上方
  - wrap-reverse - 换行，翻转
- flex-flow - 以上两个属性的简写方式
- justify-content 项目在主轴上的对齐方式
  - flex-start - 在主轴上由左或者上开始排列
  - flex-end - 在主轴上由右或者下开始排列
  - center - 在主轴上居中排列
  - space-between - 在主轴上左右两端或者上下两端开始排列
  - space-around - 每个项目两侧的间隔相等，所以，项目之间的间隔比项目与边框的间隔大一倍
- align-items - 项目在交叉轴上对齐方式
  - flex-start - 由上开始排列
  - flex-end - 由下开始排列
  - center - 居中排列
  - baseline - 根据字体排列
  - stretch - 拉长排列
- align-content - 定义了多根轴线的对齐方式，如果项目只有一根轴线，该属性不起作用

grid - 网格布局，将网页划分成一个个的网格，可以任意组合不同的网格，做出各种各样的布局

- 声明 - display: grid;
- 设置每个列之间的宽度 - grid-template-columns: px px px...;  --- 使用fr会自动按比例划分
- 设置列间距 - column-gap: 24px
- 设置行间距 - row-gap: 24px
- 统一设置间距 - gap:
- 排列元素 - grid-template-areas
  - ![image-20210415194504536](C:\Users\28051\Desktop\笔记\image-20210415194504536.png)
  - ![image-20210415194539155](C:\Users\28051\Desktop\笔记\image-20210415194539155.png)
  - ![image-20210415194602393](C:\Users\28051\Desktop\笔记\图片笔记\image-20210415194602393.png)
- 行列块内纵轴对齐 - align-items:
- 行列块内横轴对齐 - justify-items:
- 对行列块对齐 - align-content
- 行列块横轴对齐 - justify-content

grid个flex布局的区别 - flex是轴线布局，只能指定项目针对轴线的位置，可以看做是一维布局，grid布局则是将容器划分成行和列，产生单元格，然后指定项目项目所在的单元格，可以看做是二维布局，=

### 改变元素的类型

display - 属性规定元素应该生成的框的类型

- none - 此元素不会被显示
- block - 此元素将显示为块级元素，该元素前后会带有换行符
- inline - 默认，该元素会被显示为内联元素，元素前后没有换行符
- inline-block - 行内块元素
- list-item - 该元素会被作为列表元素显示
- run-in - 此元素会根据上下文作为块级元素或内联元素显示
- table- 此元素会作为块级表格来显示，table，表格前后带有换行符
- inline-table - 此元素会作为内联表格来显示，表格前后没有换行符
- table-row-group - 此元素会作为一个或多个行的分组来显示 tbody
- table-header-group - 此元素会作为一个或多个行的分组来显示 thead
- table-footer-group - 此元素会作为一个或多个行的分组来显示 tfoot
- table-row - 此元素会作为一个表格行显示 tr
- table-column-group 此元素会作为一个或多个列的分组来显示 colgroup
- table-column - 此元素会作为一个单元格列显示 col
- table-cell - 此元素会作为一个表格单元格显示 td和th
- table-caption - 此元素会作为一个表格标题显示 caption
- flex - flexible box的缩写，意为弹性布局，用来为盒状模型提供最大的灵活性-子元素的float，clear，vertical-align属性将失效

### 元素大小

min-height - 设置元素的最小高度

- length - 定义元素的最小高度，默认值是0
- % - 定义基于包含它的块级对象的百分比最小高度

#### 元素透明度

opacity - 设置元素的不透明级别

- value - 0(完全不透明)~1(完全透明)之间，

### 元素边框

padding - 设置元素的4个内边距

- 顺时针方向

margin - 设置元素的4个外边距

- 顺时针方向

boder-radius -  是一个最多可指定四个border -*- radius属性的符合属性

- 逆时针方向

### 文本修饰

text-decoration - 规定添加到文本的修饰

- none - 默认，定义标准的文本
- underline - 定义文本下的一条线
- overline - 定义文本上的一条线
- line-through - 定义穿过文本的下的一条线
- blink - 定义闪烁的文本

text-transform - 控制文本的大小写

- none - 默认，定义带有小写字母和大写字母的标准文本
- capitalize - 文本中的每个单词以大写字母开头
- uppercase - 定义仅有大写字母
- lowercase - 定义仅有小写字母

letter-spacing - 增加或减少字符间的空白

- normal - 默认，规定字符间没有额外的空间
- length - 定义字符间的固定空间

### 选择器

:nth-child(n) - 匹配属于其父元素的第n个子元素，不论元素类型

#### 内容溢出

overflow - 当内容溢出后发生的事情

- visible - 默认，内容不会被修剪，会呈现在元素框之外
- hidden - 内容会被修剪，并且其余内容不可见
- scroll - 内容会被修剪，但是浏览器会显示滚动条以便查看其余内容
- auto - 如果内容被修剪，则浏览器会显示滚动条以便查看其余内容