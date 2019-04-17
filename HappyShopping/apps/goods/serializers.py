from rest_framework import serializers

from goods.models import Goods, GoodsCategory


 #class GoodsSerializer(serializers.Serializer):
 #    name = serializers.CharField(required=True, max_length=100)
 #    click_num = serializers.IntegerField(default=0)
 #    goods_front_image = serializers.ImageField()
 #
 #    # drf 默认会将所有字段值放在 validated_data 参数中
 #    def create(self, validated_data):
 #        """
 #        创建对象
 #        """
 #        return Goods.objects.create(**validated)
 #


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    # Goods模型类的外键，实现序列化嵌套
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"

