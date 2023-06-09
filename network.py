import torch.nn.functional as F
import torch.nn as nn
import torch
import torchvision
from torchsummary import summary

def model_resnet101(num_classes):
    '''
    resnet101
    '''
    # 載入 ResNet101 預訓練模型
    resnet101 = torchvision.models.resnet101(pretrained=True, progress=True)
    # 鎖定 ResNet101 預訓練模型參數
    for param in resnet101.parameters():
        param.requires_grad = False
    # 取得 ResNet101 最後一層的輸入特徵數量
    num_ftrs = resnet101.fc.in_features
    # 將 ResNet101 的最後一層改為只有兩個輸出線性層
    # 更一般化的寫法為 nn.Linear(num_ftrs, len(class_names))
    resnet101.fc = nn.Linear(num_ftrs, num_classes)
    return resnet101

def model_resnet50(num_classes):
    '''
    resnet50
    '''
    # 載入 ResNet50 預訓練模型
    resnet50 = torchvision.models.resnet50(pretrained=True, progress=True)
    # 鎖定 ResNet50 預訓練模型參數
    for param in resnet50.parameters():
        param.requires_grad = False
    # 取得 ResNet50 最後一層的輸入特徵數量
    num_ftrs = resnet50.fc.in_features
    # 將 ResNet50 的最後一層改為只有兩個輸出線性層
    # 更一般化的寫法為 nn.Linear(num_ftrs, len(class_names))
    resnet50.fc = nn.Linear(num_ftrs, num_classes)
    return resnet50

def model_densenet121(num_classes):
    '''
    densenet121
    '''
    # 載入 densenet121 預訓練模型
    densenet121 = torchvision.models.densenet121(pretrained=True, progress=True)
    # 鎖定 densenet121 預訓練模型參數
    for param in densenet121.parameters():
        param.requires_grad = False
    # 取得 densenet121 最後一層的輸入特徵數量
    num_ftrs = densenet121.classifier.in_features
    # 將 densenet121 的最後一層改為只有兩個輸出線性層
    # 更一般化的寫法為 nn.Linear(num_ftrs, len(class_names))
    densenet121.classifier = nn.Linear(num_ftrs, num_classes)
    return densenet121

def model_densenet161(num_classes):
    '''
    densenet161
    '''
    # 載入 densenet161 預訓練模型
    densenet161 = torchvision.models.densenet161(pretrained=True, progress=True)
    # 鎖定 densenet161 預訓練模型參數
    for param in densenet161.parameters():
        param.requires_grad = False
    # 取得 densenet161 最後一層的輸入特徵數量
    num_ftrs = densenet161.classifier.in_features
    # 將 densenet161 的最後一層改為只有兩個輸出線性層
    # 更一般化的寫法為 nn.Linear(num_ftrs, len(class_names))
    densenet161.classifier = nn.Linear(num_ftrs, num_classes)
    return densenet161

def model_densenet201(num_classes):
    '''
    densenet201
    '''
    # 載入 densenet201 預訓練模型
    densenet201 = torchvision.models.densenet201(pretrained=True, progress=True)
    # 鎖定 densenet201 預訓練模型參數
    for param in densenet201.parameters():
        param.requires_grad = False
    # 取得 densenet201 最後一層的輸入特徵數量
    num_ftrs = densenet201.classifier.in_features
    # 將 densenet201 的最後一層改為只有兩個輸出線性層
    # 更一般化的寫法為 nn.Linear(num_ftrs, len(class_names))
    densenet201.classifier = nn.Linear(num_ftrs, num_classes)
    return densenet201

def model_efficientnet_b0(num_classes):
    '''
    efficientnet_b0
    '''
    # 載入 efficientnet_b0 預訓練模型
    efficientnet_b0 = torchvision.models.efficientnet_b0(pretrained=True, progress=True)
    # 鎖定 efficientnet_b0 預訓練模型參數
    for param in efficientnet_b0.parameters():
        param.requires_grad = False
    # 取得 efficientnet_b0 最後一層的輸入特徵數量
    num_ftrs = efficientnet_b0.classifier[1].in_features
    efficientnet_b0.classifier[1] = nn.Linear(num_ftrs, num_classes) # type: ignore
    return efficientnet_b0

def model_efficientnet_b4(num_classes):
    '''
    efficientnet_b4
    '''
    # 載入 efficientnet_b4 預訓練模型
    efficientnet_b4 = torchvision.models.efficientnet_b4(pretrained=True, progress=True)
    # 鎖定 efficientnet_b4 預訓練模型參數
    for param in efficientnet_b4.parameters():
        param.requires_grad = False
    # 取得 efficientnet_b4 最後一層的輸入特徵數量
    num_ftrs = efficientnet_b4.classifier[1].in_features
    efficientnet_b4.classifier[1] = nn.Linear(num_ftrs, num_classes) # type: ignore
    return efficientnet_b4

def model_efficientnet_b7(num_classes):
    '''
    efficientnet_b7
    '''
    # 載入 efficientnet_b4 預訓練模型
    efficientnet_b7 = torchvision.models.efficientnet_b7(pretrained=True, progress=True)
    # 鎖定 efficientnet_b4 預訓練模型參數
    for param in efficientnet_b7.parameters():
        param.requires_grad = False
    # 取得 efficientnet_b4 最後一層的輸入特徵數量
    num_ftrs = efficientnet_b7.classifier[1].in_features
    efficientnet_b7.classifier[1] = nn.Linear(num_ftrs, num_classes) # type: ignore
    return efficientnet_b7

def model_efficientnet_v2_s(num_classes):
    '''
    efficientnet_v2_s
    '''
    # 載入 efficientnet_v2_s 預訓練模型
    efficientnet_v2_s = torchvision.models.efficientnet_v2_s(pretrained=True, progress=True)
    # 鎖定efficientnet_v2_s 預訓練模型參數
    for param in efficientnet_v2_s.parameters():
        param.requires_grad = False
    # 取得 efficientnet_v2_s 最後一層的輸入特徵數量
    num_ftrs = efficientnet_v2_s.classifier[1].in_features
    efficientnet_v2_s.classifier[1] = nn.Linear(num_ftrs, num_classes) # type: ignore
    return efficientnet_v2_s

def model_efficientnet_v2_l(num_classes):
    '''
    efficientnet_v2_l
    '''
    # 載入 efficientnet_v2_l 預訓練模型
    efficientnet_v2_l = torchvision.models.efficientnet_v2_l(pretrained=True, progress=True)
    # efficientnet_v2_l 預訓練模型參數
    for param in efficientnet_v2_l.parameters():
        param.requires_grad = False
    # 取得 efficientnet_v2_l 最後一層的輸入特徵數量
    num_ftrs = efficientnet_v2_l.classifier[1].in_features
    efficientnet_v2_l.classifier[1] = nn.Linear(num_ftrs, num_classes) # type: ignore
    return efficientnet_v2_l

def model_efficientnet_v2_l_trainable(num_classes):
    '''
    efficientnet_v2_l
    '''
    # 載入 efficientnet_v2_l 預訓練模型
    efficientnet_v2_l = torchvision.models.efficientnet_v2_l(pretrained=True, progress=True)
    # efficientnet_v2_l 預訓練模型參數
    #for param in efficientnet_v2_l.parameters():
    #   param.requires_grad = False
    # 取得 efficientnet_v2_l 最後一層的輸入特徵數量
    num_ftrs = efficientnet_v2_l.classifier[1].in_features
    efficientnet_v2_l.classifier[1] = nn.Linear(num_ftrs, num_classes) # type: ignore
    return efficientnet_v2_l

def model_efficientnet_v2_l_no_pretain(num_classes):
    '''
    efficientnet_v2_l
    '''
    # 載入 efficientnet_v2_l 預訓練模型
    efficientnet_v2_l = torchvision.models.efficientnet_v2_l(pretrained=False, progress=True)
    efficientnet_v2_l.features[0][0] = nn.Conv2d(1, 32, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
    #print(efficientnet_v2_l.features[0][0])
    # 取得 efficientnet_v2_l 最後一層的輸入特徵數量
    num_ftrs = efficientnet_v2_l.classifier[1].in_features
    efficientnet_v2_l.classifier[1] = nn.Linear(num_ftrs, num_classes) # type: ignore
    return efficientnet_v2_l

def model_resnext101_64x4d(num_classes):
    '''
    resnext101_64x4d
    '''
    # 載入 resnext101_64x4d 預訓練模型
    resnext101_64x4d = torchvision.models.resnext101_64x4d(pretrained=True, progress=True)
    # resnext101_64x4d 預訓練模型參數
    for param in resnext101_64x4d.parameters():
        param.requires_grad = False
    # 取得 resnext101_64x4d 最後一層的輸入特徵數量
    num_ftrs = resnext101_64x4d.fc.in_features
    resnext101_64x4d.fc = nn.Linear(num_ftrs, num_classes) # type: ignore
    return resnext101_64x4d

def model_vit_b_16(num_classes):
    '''
    vit_b_16
    '''
    # 載入 vit_b_16 預訓練模型
    vit_b_16 = torchvision.models.vit_b_16(pretrained=True, progress=True)
    # vit_b_16 預訓練模型參數
    for param in vit_b_16.parameters():
        param.requires_grad = False
    # 取得 vit_b_16 最後一層的輸入特徵數量
    num_ftrs = vit_b_16.heads.head.in_features
    vit_b_16.fc = nn.Linear(num_ftrs, num_classes) # type: ignore
    return vit_b_16

def model_regnet_y_128gf(num_classes):
    '''
    regnet_y_128gf
    '''
    # 載入 regnet_y_128gf 預訓練模型
    regnet_y_128gf = torchvision.models.regnet_y_128gf(weights='DEFAULT', progress=True)
    # regnet_y_128gf 預訓練模型參數
    for param in regnet_y_128gf.parameters():
        param.requires_grad = False
    # 取得 regnet_y_128gf 最後一層的輸入特徵數量
    num_ftrs = regnet_y_128gf.fc.in_features
    regnet_y_128gf.fc = nn.Linear(num_ftrs, num_classes) # type: ignore
    return regnet_y_128gf

def model_regnet_y_16gf(num_classes):
    '''
    regnet_y_16gf
    '''
    # 載入 regnet_y_16gf 預訓練模型
    regnet_y_16gf = torchvision.models.regnet_y_16gf(weights='DEFAULT', progress=True)
    # regnet_y_16gf 預訓練模型參數
    for param in regnet_y_16gf.parameters():
        param.requires_grad = False
    # 取得 regnet_y_16gf 最後一層的輸入特徵數量
    num_ftrs = regnet_y_16gf.fc.in_features
    regnet_y_16gf.fc = nn.Linear(num_ftrs, num_classes) # type: ignore
    return regnet_y_16gf

def model_mobilenet_v3_small(num_classes):
    '''
    mobilenet_v3_small
    '''
    # 載入 mobilenet_v3_small 預訓練模型
    mobilenet_v3_small = torchvision.models.mobilenet_v3_small(pretrained=True, progress=True)
    # mobilenet_v3_small 預訓練模型參數
    for param in mobilenet_v3_small.parameters():
        param.requires_grad = False
    # 取得 mobilenet_v3_small 最後一層的輸入特徵數量
    num_ftrs = mobilenet_v3_small.classifier[3].in_features
    mobilenet_v3_small.classifier[3] = nn.Linear(num_ftrs, num_classes) # type: ignore
    return mobilenet_v3_small

def model_mobilenet_v3_large(num_classes):
    '''
    mobilenet_v3_large
    '''
    # 載入 mobilenet_v3_large 預訓練模型
    mobilenet_v3_large = torchvision.models.mobilenet_v3_large(pretrained=True, progress=True)
    # mobilenet_v3_large 預訓練模型參數
    for param in mobilenet_v3_large.parameters():
        param.requires_grad = False
    # 取得 mobilenet_v3_large 最後一層的輸入特徵數量
    num_ftrs = mobilenet_v3_large.classifier[3].in_features
    mobilenet_v3_large.classifier[3] = nn.Linear(num_ftrs, num_classes) # type: ignore
    return mobilenet_v3_large

if __name__ == '__main__':
    #GPU
    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    print('GPU state:',device)
    #net = cnn_conv2(10).to(device)
    #print(net)
    #print(summary(net, input_size=(3,32,32)))
    #model_efficientnet_v2_l_no_pretain(6)
    print(model_efficientnet_v2_l_no_pretain(6))