# ����ǩ���� - CI ��

* �ɰٶȷ������û��������������Ÿ�ȫ�����ѽ���ʹ�á�  
* �޷�Խ� Travis CI��ȫ�Զ�ȫ�������ֵ�أ����ܼ�أ��ܾ�©ǩ��
* ģ��ͻ���ǩ������ǩ+6������+8��
* ���ÿ�Դ��Э����ɡ�

## �÷�

### ������

```
pip install -r requirement.txt
echo "��� BDUSS" > cookie
python main.py
```

### Travis CI

1��fork �����Ŀ

2������`.travis.yml`��`env.global`���֡�

+   `GH_UN`����� Github �û����������ύ��
+   `GH_EMAIL`����� Github ���䣨�����ύ��
+   `GH_USER`���ֿ����ڵ��û�
+   `GH_REPO`���ֿ�����
+   `GH_BRANCH`��Ҫ�ύ�ķ�֧

3������`travis-ci.org/{�û���}/{�ֿ�}`������ CI��

![](http://ww1.sinaimg.cn/large/841aea59ly1fxd7aw17xtj20n50ig759.jpg)

4���ڻ�������������`BDUSS`����ʽΪ`BDUSS=.{192}`����ȡ��������һ�ڡ�

![](http://ww1.sinaimg.cn/large/841aea59ly1fxd7pe6becj213b0apq3p.jpg)

5������ CRON��

![](http://ww1.sinaimg.cn/large/841aea59ly1fxd7cctc2vj212y059jrg.jpg)

## ��ȡCookie��Chrome��

1. �����ڰٶ�����ҳ���ϵ�¼����˺š�
2. ��ַ��������`chrome://settings/cookies`��
3. �����Ĵ������Ͻ��ı���������`tieba.com`��
4. �ҵ���վΪ`tieba.com`����Ŀ����������ҵ�`BDUSS`��ǩ�������
5. `����`��������Ҫ���ַ�������ͬ`BDUSS=`һ�����뵽ҳ���ϵ��ı����С�

![cookie](http://ww4.sinaimg.cn/large/841aea59gw1eirbls65ryj20k20ew759.jpg)

## ά��

���ڰٶ����ɿ���Ƶ��������ӿڣ�����������ɲ������֣���`tbops.py`�е��������ɲ���������������ĵ��ַ�������һ�� Python �������û��������޸ġ�

> ����ʵ֤�������ҿ�ʼ�����ɵ� 2012 �굽���ڣ���Щ�ӿڴ���û��ʧЧ��

## ����

�κη������ύ�� ISSUE��
